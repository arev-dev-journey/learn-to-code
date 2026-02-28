import logging
from collections.abc import Generator

from fastapi import Depends, FastAPI, Header, HTTPException, Response
from sqlalchemy.orm import Session

from .ai import summarize_failed_events
from .config import get_settings
from .db import get_session, init_db
from .logging_config import configure_logging
from .metrics import INGEST_REQUESTS, EVENT_PROCESSING, SYNC_DURATION, render_metrics
from .queue import QueueClient, build_queue_client
from .schemas import AIErrorSummary, EventIn, IngestInventoryRequest, InventoryRecord, PartnerInventoryRecord, SyncResult
from .services import (
    enqueue_event,
    ingest_inventory,
    process_sync_batch,
    read_canonical_inventory,
    read_failed_events,
    read_partner_inventory,
)

configure_logging()
logger = logging.getLogger(__name__)
settings = get_settings()

app = FastAPI(title=settings.app_name, version='1.0.0')
queue_client = build_queue_client()


def get_db_session() -> Generator[Session, None, None]:
    yield from get_session()


def get_queue_client() -> QueueClient:
    return queue_client


def require_api_key(x_api_key: str = Header(default='')) -> None:
    if x_api_key != settings.api_key:
        raise HTTPException(status_code=401, detail='invalid API key')


@app.on_event('startup')
def startup() -> None:
    init_db()
    logger.info('application started')


@app.get('/health')
def health() -> dict[str, str]:
    return {'status': 'ok'}


@app.get('/metrics')
def metrics() -> Response:
    payload, content_type = render_metrics()
    return Response(content=payload, media_type=content_type)


@app.post('/v1/partners/{partner_id}/inventory')
def ingest_partner_inventory(
    partner_id: str,
    request: IngestInventoryRequest,
    session: Session = Depends(get_db_session),
    queue: QueueClient = Depends(get_queue_client),
    _: None = Depends(require_api_key),
) -> dict:
    INGEST_REQUESTS.labels(partner_id=partner_id).inc()
    try:
        count = ingest_inventory(session, queue, partner_id, request)
        session.commit()
    except Exception as exc:  # noqa: BLE001
        session.rollback()
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return {'partner_id': partner_id, 'ingested_items': count}


@app.post('/v1/events')
def submit_event(
    event: EventIn,
    session: Session = Depends(get_db_session),
    queue: QueueClient = Depends(get_queue_client),
    _: None = Depends(require_api_key),
) -> dict[str, str]:
    enqueue_event(session, queue, event)
    session.commit()
    return {'status': 'queued'}


@app.post('/v1/sync/run', response_model=SyncResult)
def run_sync(
    session: Session = Depends(get_db_session),
    _: None = Depends(require_api_key),
) -> SyncResult:
    with SYNC_DURATION.time():
        processed, failed = process_sync_batch(session)
        session.commit()
    EVENT_PROCESSING.labels(status='processed').inc(processed)
    EVENT_PROCESSING.labels(status='failed').inc(failed)
    return SyncResult(processed_events=processed, failed_events=failed)


@app.get('/v1/partners/{partner_id}/inventory', response_model=list[PartnerInventoryRecord])
def partner_inventory(
    partner_id: str,
    session: Session = Depends(get_db_session),
    _: None = Depends(require_api_key),
) -> list[PartnerInventoryRecord]:
    rows = read_partner_inventory(session, partner_id)
    return [PartnerInventoryRecord.model_validate(row, from_attributes=True) for row in rows]


@app.get('/v1/inventory/{sku}', response_model=InventoryRecord)
def canonical_inventory(
    sku: str,
    session: Session = Depends(get_db_session),
    _: None = Depends(require_api_key),
) -> InventoryRecord:
    row = read_canonical_inventory(session, sku.upper())
    if row is None:
        raise HTTPException(status_code=404, detail='sku not found')
    return InventoryRecord.model_validate(row, from_attributes=True)


@app.get('/v1/ai/failures/summary', response_model=AIErrorSummary)
def ai_failure_summary(
    session: Session = Depends(get_db_session),
    _: None = Depends(require_api_key),
) -> AIErrorSummary:
    failures = read_failed_events(session)
    summary, generated_by = summarize_failed_events(failures)
    return AIErrorSummary(summary=summary, generated_by=generated_by)
