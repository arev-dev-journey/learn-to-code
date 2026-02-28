import logging
import time

from .db import SessionLocal, init_db
from .logging_config import configure_logging
from .metrics import EVENT_PROCESSING, SYNC_DURATION
from .services import process_sync_batch

configure_logging()
logger = logging.getLogger(__name__)


def run_forever(poll_interval: float = 2.0) -> None:
    init_db()
    logger.info('worker started')
    while True:
        with SessionLocal() as session:
            with SYNC_DURATION.time():
                processed, failed = process_sync_batch(session)
                session.commit()
            if processed or failed:
                EVENT_PROCESSING.labels(status='processed').inc(processed)
                EVENT_PROCESSING.labels(status='failed').inc(failed)
                logger.info('batch processed', extra={'processed': processed, 'failed': failed})
        time.sleep(poll_interval)


if __name__ == '__main__':
    run_forever()
