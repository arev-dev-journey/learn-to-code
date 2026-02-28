# Partner Inventory Sync System

Production-style backend starter for partner inventory ingestion and synchronization, inspired by ticket marketplace integrations.

## 1) High-level architecture overview

```
Partner System
   |
   | REST (API key)
   v
+------------------------+         +--------------------+
| FastAPI API Service    |         |  Prometheus scrape |
| - validation/normalize |----->   |  /metrics          |
| - writes partner state |         +--------------------+
| - emits domain events  |
+-----------+------------+
            |
            | queue publish (db queue locally, SQS in AWS)
            v
+------------------------+
| Queue Events           |
| (Postgres table/SQS)   |
+-----------+------------+
            |
            v
+------------------------+       +------------------------------+
| Worker Service         |-----> | Canonical Inventory Material |
| - polls queue          |       | View (aggregated by SKU)     |
| - sync pipeline        |       +------------------------------+
| - marks failures       |
+-----------+------------+
            |
            v
+------------------------+
| AI Failure Summarizer  |
| OpenAI-compatible API  |
| + fallback rules       |
+------------------------+
```

## 2) Project folder structure

```
partner-inventory-sync/
├── app/
│   ├── ai.py
│   ├── config.py
│   ├── db.py
│   ├── logging_config.py
│   ├── main.py
│   ├── metrics.py
│   ├── models.py
│   ├── normalizer.py
│   ├── queue.py
│   ├── schemas.py
│   ├── services.py
│   └── worker.py
├── infra/aws/ecs-fargate.yaml
├── tests/test_api.py
├── Dockerfile
├── Dockerfile.worker
├── docker-compose.yml
├── requirements.txt
└── requirements-dev.txt
```

## 3) Step-by-step implementation

1. **Partner ingestion API**: `POST /v1/partners/{partner_id}/inventory` accepts upsert/delete actions.
2. **Normalization/validation**: SKU normalization (`trim + uppercase`) and business validation (`delete => quantity=0`).
3. **Eventing**: every ingest emits an `INVENTORY_CHANGED` event through pluggable queue backend.
4. **Async processing**: worker claims pending events and materializes canonical inventory totals.
5. **Read models**: partner-level and canonical SKU read endpoints.
6. **Observability**: JSON structured logs + Prometheus metrics.
7. **AI feature**: `/v1/ai/failures/summary` summarizes failed queue events using OpenAI-compatible API.

## 4) Complete code for each component

See source files directly:
- API entrypoint and endpoints: `app/main.py`
- Domain and orchestration logic: `app/services.py`
- Queue adapters (DB + SQS): `app/queue.py`
- Data models and persistence: `app/models.py`, `app/db.py`
- AI summarizer abstraction: `app/ai.py`
- Worker process: `app/worker.py`

## 5) Data flow explanation

1. Partner calls ingestion endpoint with API key.
2. API normalizes payload and persists partner inventory rows.
3. API writes queue event.
4. Worker polls queue and recomputes canonical inventory view.
5. Read APIs serve canonical/partner state.
6. If processing fails, failures are visible and summarized by AI endpoint.

## API surface

- `GET /health`
- `GET /metrics`
- `POST /v1/partners/{partner_id}/inventory`
- `POST /v1/events`
- `POST /v1/sync/run` (manual trigger for demo/local)
- `GET /v1/partners/{partner_id}/inventory`
- `GET /v1/inventory/{sku}`
- `GET /v1/ai/failures/summary`

> All `/v1/*` APIs require `x-api-key`.

## Local setup instructions

### Option A: Docker Compose (recommended)

```bash
docker compose up --build
```

### Option B: Run API locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
export DATABASE_URL='postgresql+psycopg://postgres:postgres@localhost:5432/inventory'
export PARTNER_API_KEY='dev-partner-key'
uvicorn app.main:app --reload
```

Run worker:

```bash
python -m app.worker
```

Run tests:

```bash
pytest
```

## Example API usage

```bash
curl -X POST 'http://localhost:8000/v1/partners/acme/inventory' \
  -H 'x-api-key: dev-partner-key' \
  -H 'content-type: application/json' \
  -d '{"items":[{"sku":" sku-1 ","quantity":5,"action":"upsert"}]}'

curl -X POST 'http://localhost:8000/v1/sync/run' -H 'x-api-key: dev-partner-key'
curl 'http://localhost:8000/v1/inventory/SKU-1' -H 'x-api-key: dev-partner-key'
curl 'http://localhost:8000/v1/ai/failures/summary' -H 'x-api-key: dev-partner-key'
```

## Cloud readiness (AWS ECS/EC2)

- Dockerized API and worker images.
- Environment-variable-driven config.
- SQS adapter available via `QUEUE_BACKEND=sqs` + `SQS_QUEUE_URL`.
- Existing `infra/aws/ecs-fargate.yaml` can be extended to include:
  - RDS PostgreSQL
  - SQS queue
  - separate worker ECS service

### Suggested production env vars

- `DATABASE_URL`
- `PARTNER_API_KEY`
- `QUEUE_BACKEND=db|sqs`
- `SQS_QUEUE_URL`
- `AWS_REGION`
- `LLM_BASE_URL`
- `LLM_API_KEY`
- `LLM_MODEL`

## Scaling considerations

- Scale API horizontally behind ALB; stateless design.
- Scale workers independently by queue depth.
- Use partitioning and indexes on `partner_inventory` and queue table.
- For high throughput: switch from DB queue to SQS + idempotent event handlers.
- Add dead-letter queue and retry backoff policy.

## Failure modes

- **Bad payloads**: rejected at validation layer with 400.
- **Worker failures**: events marked `failed` with error message.
- **Queue outage**: fall back to DB queue in local mode.
- **LLM outage**: AI endpoint gracefully returns deterministic rules summary.
- **DB outage**: API fails fast; health checks detect non-ready state.

## Future improvements

- Add Alembic migrations.
- Add idempotency keys on ingest endpoint.
- Add async SQS consumer with long polling and DLQ.
- Add OpenTelemetry tracing.
- Add authN/authZ beyond API key.
- Introduce CDC/outbox pattern for strict delivery guarantees.
