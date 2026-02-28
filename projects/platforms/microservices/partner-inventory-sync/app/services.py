import json
import logging
from datetime import datetime, timezone

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from .models import CanonicalInventory, PartnerInventory, QueueEvent, QueueStatus
from .normalizer import normalize_payload
from .queue import QueueClient, claim_pending_events
from .schemas import EventIn, IngestInventoryRequest

logger = logging.getLogger(__name__)


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def ingest_inventory(session: Session, queue_client: QueueClient, partner_id: str, request: IngestInventoryRequest) -> int:
    normalized_items = [normalize_payload(item) for item in request.items]
    for item in normalized_items:
        existing = session.get(PartnerInventory, {'partner_id': partner_id, 'sku': item.sku})
        if item.action == 'delete':
            if existing:
                session.delete(existing)
            continue
        if existing:
            existing.quantity = item.quantity
            existing.updated_at = now_utc()
        else:
            session.add(PartnerInventory(partner_id=partner_id, sku=item.sku, quantity=item.quantity, updated_at=now_utc()))

    queue_client.publish(
        session,
        source=f'partner:{partner_id}',
        event_type='INVENTORY_CHANGED',
        payload={'partner_id': partner_id, 'items': [item.model_dump() for item in normalized_items]},
    )
    return len(normalized_items)


def enqueue_event(session: Session, queue_client: QueueClient, event: EventIn) -> None:
    queue_client.publish(session, event.source, event.event_type, event.payload)


def process_sync_batch(session: Session, batch_size: int = 100) -> tuple[int, int]:
    processed, failed = 0, 0
    events = claim_pending_events(session, batch_size)
    if not events:
        return 0, 0

    for event in events:
        try:
            _materialize_canonical_inventory(session)
            event.status = QueueStatus.processed
            event.error_message = None
            processed += 1
        except Exception as exc:  # noqa: BLE001
            event.status = QueueStatus.failed
            event.error_message = str(exc)
            event.attempt_count += 1
            failed += 1
            logger.exception('Event processing failed', extra={'event_id': event.id, 'event_type': event.event_type})

    return processed, failed


def _materialize_canonical_inventory(session: Session) -> None:
    aggregate_rows = session.execute(
        select(PartnerInventory.sku, func.sum(PartnerInventory.quantity).label('total_quantity')).group_by(PartnerInventory.sku)
    ).all()
    known_skus = set()
    for sku, total_quantity in aggregate_rows:
        known_skus.add(sku)
        canonical = session.get(CanonicalInventory, sku)
        if canonical:
            canonical.total_quantity = int(total_quantity)
            canonical.updated_at = now_utc()
        else:
            session.add(CanonicalInventory(sku=sku, total_quantity=int(total_quantity), updated_at=now_utc()))

    for stale in session.scalars(select(CanonicalInventory)).all():
        if stale.sku not in known_skus:
            session.delete(stale)


def read_partner_inventory(session: Session, partner_id: str) -> list[PartnerInventory]:
    return session.scalars(select(PartnerInventory).where(PartnerInventory.partner_id == partner_id).order_by(PartnerInventory.sku.asc())).all()


def read_canonical_inventory(session: Session, sku: str) -> CanonicalInventory | None:
    return session.get(CanonicalInventory, sku)


def read_failed_events(session: Session, limit: int = 20) -> list[QueueEvent]:
    return session.scalars(
        select(QueueEvent).where(QueueEvent.status == QueueStatus.failed).order_by(QueueEvent.updated_at.desc()).limit(limit)
    ).all()
