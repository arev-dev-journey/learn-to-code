import json
import logging
from abc import ABC, abstractmethod

import boto3
from sqlalchemy import select
from sqlalchemy.orm import Session

from .config import get_settings
from .models import QueueEvent, QueueStatus

logger = logging.getLogger(__name__)


class QueueClient(ABC):
    @abstractmethod
    def publish(self, session: Session, source: str, event_type: str, payload: dict) -> None:
        raise NotImplementedError


class DatabaseQueueClient(QueueClient):
    def publish(self, session: Session, source: str, event_type: str, payload: dict) -> None:
        session.add(QueueEvent(source=source, event_type=event_type, payload=json.dumps(payload), status=QueueStatus.pending))


class SQSQueueClient(QueueClient):
    def __init__(self, queue_url: str, region: str):
        self.queue_url = queue_url
        self.client = boto3.client('sqs', region_name=region)

    def publish(self, session: Session, source: str, event_type: str, payload: dict) -> None:
        body = {'source': source, 'event_type': event_type, 'payload': payload}
        self.client.send_message(QueueUrl=self.queue_url, MessageBody=json.dumps(body))
        session.add(QueueEvent(source=source, event_type=event_type, payload=json.dumps(payload), status=QueueStatus.pending))


def build_queue_client() -> QueueClient:
    settings = get_settings()
    if settings.queue_backend == 'sqs' and settings.sqs_queue_url:
        logger.info('Using SQS queue backend')
        return SQSQueueClient(settings.sqs_queue_url, settings.aws_region)
    logger.info('Using database queue backend')
    return DatabaseQueueClient()


def claim_pending_events(session: Session, batch_size: int = 100) -> list[QueueEvent]:
    events = session.scalars(
        select(QueueEvent)
        .where(QueueEvent.status == QueueStatus.pending)
        .order_by(QueueEvent.id.asc())
        .limit(batch_size)
    ).all()
    for event in events:
        event.status = QueueStatus.processing
    session.flush()
    return events
