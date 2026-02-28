import json
from datetime import datetime, timezone

from .db import get_conn
from .schemas import EventIn


UTC_NOW = lambda: datetime.now(timezone.utc).isoformat()


def ingest_partner_inventory(partner_id: str, items: list[dict]) -> int:
    now = UTC_NOW()
    with get_conn() as conn:
        for item in items:
            conn.execute(
                """
                INSERT INTO partner_inventory (partner_id, sku, quantity, updated_at)
                VALUES (?, ?, ?, ?)
                ON CONFLICT(partner_id, sku) DO UPDATE
                SET quantity = excluded.quantity, updated_at = excluded.updated_at
                """,
                (partner_id, item["sku"], item["quantity"], now),
            )
        conn.execute(
            """
            INSERT INTO event_queue (source, event_type, payload, status, created_at)
            VALUES (?, ?, ?, 'pending', ?)
            """,
            (
                f"partner:{partner_id}",
                "INVENTORY_INGESTED",
                json.dumps({"partner_id": partner_id, "item_count": len(items)}),
                now,
            ),
        )
    return len(items)


def enqueue_event(event: EventIn) -> None:
    with get_conn() as conn:
        conn.execute(
            """
            INSERT INTO event_queue (source, event_type, payload, status, created_at)
            VALUES (?, ?, ?, 'pending', ?)
            """,
            (event.source, event.event_type, json.dumps(event.payload), UTC_NOW()),
        )


def run_sync() -> tuple[int, int]:
    with get_conn() as conn:
        pending = conn.execute(
            "SELECT id FROM event_queue WHERE status='pending' ORDER BY id"
        ).fetchall()
        if not pending:
            return 0, 0

        aggregates = conn.execute(
            "SELECT sku, SUM(quantity) AS total_quantity FROM partner_inventory GROUP BY sku"
        ).fetchall()
        now = UTC_NOW()
        for row in aggregates:
            conn.execute(
                """
                INSERT INTO canonical_inventory (sku, total_quantity, updated_at)
                VALUES (?, ?, ?)
                ON CONFLICT(sku) DO UPDATE
                SET total_quantity = excluded.total_quantity, updated_at = excluded.updated_at
                """,
                (row["sku"], int(row["total_quantity"]), now),
            )

        conn.executemany(
            "UPDATE event_queue SET status='processed' WHERE id=?",
            [(row["id"],) for row in pending],
        )
        return len(pending), len(aggregates)


def get_partner_inventory(partner_id: str) -> list[dict]:
    with get_conn() as conn:
        rows = conn.execute(
            "SELECT sku, quantity, updated_at FROM partner_inventory WHERE partner_id=? ORDER BY sku",
            (partner_id,),
        ).fetchall()
        return [dict(row) for row in rows]


def get_canonical_inventory(sku: str) -> dict | None:
    with get_conn() as conn:
        row = conn.execute(
            "SELECT sku, total_quantity, updated_at FROM canonical_inventory WHERE sku=?",
            (sku,),
        ).fetchone()
        return dict(row) if row else None


def list_low_stock(threshold: int) -> list[dict]:
    with get_conn() as conn:
        rows = conn.execute(
            "SELECT sku, total_quantity, updated_at FROM canonical_inventory WHERE total_quantity <= ? ORDER BY total_quantity ASC",
            (threshold,),
        ).fetchall()
        return [dict(row) for row in rows]
