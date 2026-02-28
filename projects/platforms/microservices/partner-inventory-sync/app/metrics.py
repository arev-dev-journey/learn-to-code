from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

INGEST_REQUESTS = Counter('inventory_ingest_requests_total', 'Total inventory ingest requests', ['partner_id'])
EVENT_PROCESSING = Counter('inventory_events_processed_total', 'Events processed', ['status'])
SYNC_DURATION = Histogram('inventory_sync_duration_seconds', 'Sync event processing duration')


def render_metrics() -> tuple[bytes, str]:
    return generate_latest(), CONTENT_TYPE_LATEST
