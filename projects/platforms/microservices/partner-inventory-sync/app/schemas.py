from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel, Field, field_validator


class InventoryItemIn(BaseModel):
    sku: str = Field(min_length=1, max_length=128)
    quantity: int = Field(ge=0)
    action: Literal['upsert', 'delete'] = 'upsert'


class IngestInventoryRequest(BaseModel):
    items: list[InventoryItemIn] = Field(min_length=1)


class EventIn(BaseModel):
    source: str
    event_type: str
    payload: dict[str, Any]


class InventoryRecord(BaseModel):
    sku: str
    total_quantity: int
    updated_at: datetime


class PartnerInventoryRecord(BaseModel):
    partner_id: str
    sku: str
    quantity: int
    updated_at: datetime


class SyncResult(BaseModel):
    processed_events: int
    failed_events: int


class AIErrorSummary(BaseModel):
    generated_by: str
    summary: str


class NormalizedInventoryItem(BaseModel):
    sku: str
    quantity: int
    action: Literal['upsert', 'delete']

    @field_validator('sku')
    @classmethod
    def normalize_sku(cls, value: str) -> str:
        return value.strip().upper()
