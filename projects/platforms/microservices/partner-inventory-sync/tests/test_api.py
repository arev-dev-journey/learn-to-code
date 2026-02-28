import os
from pathlib import Path

from fastapi.testclient import TestClient


def test_ingest_sync_and_ai_recommendations(tmp_path: Path):
    db_path = tmp_path / "test.db"
    os.environ["INVENTORY_DB_PATH"] = str(db_path)

    from app.main import app

    client = TestClient(app)

    health = client.get("/health")
    assert health.status_code == 200

    ingest = client.post(
        "/v1/partners/acme/inventory",
        json={
            "items": [
                {"sku": "SKU-1", "quantity": 3},
                {"sku": "SKU-2", "quantity": 50},
            ]
        },
    )
    assert ingest.status_code == 200
    assert ingest.json()["ingested_items"] == 2

    sync = client.post("/v1/sync/run")
    assert sync.status_code == 200
    assert sync.json()["synchronized_skus"] == 2

    inventory = client.get("/v1/inventory/SKU-1")
    assert inventory.status_code == 200
    assert inventory.json()["total_quantity"] == 3

    ai = client.get("/v1/ai/recommendations/low-stock?threshold=5")
    assert ai.status_code == 200
    assert "SKU-1" in ai.json()["summary"]
