import os
from pathlib import Path

from fastapi.testclient import TestClient


def build_client(db_file: Path) -> TestClient:
    os.environ['DATABASE_URL'] = f'sqlite+pysqlite:///{db_file}'
    os.environ['PARTNER_API_KEY'] = 'test-key'
    os.environ['QUEUE_BACKEND'] = 'db'

    from app.config import get_settings

    get_settings.cache_clear()

    from app.main import app

    return TestClient(app)


def test_inventory_sync_and_read(tmp_path: Path):
    client = build_client(tmp_path / 'test.db')
    headers = {'x-api-key': 'test-key'}

    ingest = client.post(
        '/v1/partners/acme/inventory',
        json={'items': [{'sku': ' sku-1 ', 'quantity': 4}, {'sku': 'sku-2', 'quantity': 2}]},
        headers=headers,
    )
    assert ingest.status_code == 200
    assert ingest.json()['ingested_items'] == 2

    sync = client.post('/v1/sync/run', headers=headers)
    assert sync.status_code == 200
    assert sync.json()['processed_events'] >= 1

    inventory = client.get('/v1/inventory/SKU-1', headers=headers)
    assert inventory.status_code == 200
    assert inventory.json()['total_quantity'] == 4


def test_validation_error_for_delete_quantity(tmp_path: Path):
    client = build_client(tmp_path / 'bad.db')
    headers = {'x-api-key': 'test-key'}
    response = client.post(
        '/v1/partners/acme/inventory',
        json={'items': [{'sku': 'sku-9', 'quantity': 1, 'action': 'delete'}]},
        headers=headers,
    )
    assert response.status_code == 400
