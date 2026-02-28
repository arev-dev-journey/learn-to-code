from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class InventoryItem(BaseModel):
    sku: str = Field(min_length=1)
    quantity: int = Field(ge=0)


class IngestInventoryRequest(BaseModel):
    items: list[InventoryItem]


class EventIn(BaseModel):
    source: str
    event_type: str
    payload: dict[str, Any]


class SyncResult(BaseModel):
    processed_events: int
    synchronized_skus: int


class InventoryRecord(BaseModel):
    sku: str
    total_quantity: int
    updated_at: datetime


class AIRecommendation(BaseModel):
    summary: str
    generated_by: str
