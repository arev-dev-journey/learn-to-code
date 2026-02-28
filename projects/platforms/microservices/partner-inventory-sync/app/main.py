from datetime import datetime

from fastapi import FastAPI, HTTPException, Query

from .ai import build_low_stock_recommendation
from .db import init_db
from .schemas import AIRecommendation, EventIn, IngestInventoryRequest, InventoryRecord, SyncResult
from .services import (
    enqueue_event,
    get_canonical_inventory,
    get_partner_inventory,
    ingest_partner_inventory,
    list_low_stock,
    run_sync,
)

app = FastAPI(title="Partner Inventory Sync", version="0.1.0")


@app.on_event("startup")
def startup() -> None:
    init_db()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/v1/partners/{partner_id}/inventory")
def ingest_inventory(partner_id: str, request: IngestInventoryRequest) -> dict:
    count = ingest_partner_inventory(partner_id, [item.model_dump() for item in request.items])
    return {"partner_id": partner_id, "ingested_items": count}


@app.post("/v1/events")
def ingest_event(event: EventIn) -> dict[str, str]:
    enqueue_event(event)
    return {"status": "queued"}


@app.post("/v1/sync/run", response_model=SyncResult)
def sync_state() -> SyncResult:
    processed, sku_count = run_sync()
    return SyncResult(processed_events=processed, synchronized_skus=sku_count)


@app.get("/v1/partners/{partner_id}/inventory")
def read_partner_inventory(partner_id: str) -> dict:
    return {"partner_id": partner_id, "items": get_partner_inventory(partner_id)}


@app.get("/v1/inventory/{sku}", response_model=InventoryRecord)
def read_inventory(sku: str) -> InventoryRecord:
    row = get_canonical_inventory(sku)
    if not row:
        raise HTTPException(status_code=404, detail="sku not found")
    return InventoryRecord(
        sku=row["sku"],
        total_quantity=row["total_quantity"],
        updated_at=datetime.fromisoformat(row["updated_at"]),
    )


@app.get("/v1/ai/recommendations/low-stock", response_model=AIRecommendation)
def ai_low_stock_recommendation(threshold: int = Query(10, ge=0)) -> AIRecommendation:
    low_stock = list_low_stock(threshold)
    summary, generated_by = build_low_stock_recommendation(low_stock)
    return AIRecommendation(summary=summary, generated_by=generated_by)
