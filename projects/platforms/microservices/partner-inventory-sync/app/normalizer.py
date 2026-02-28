from .schemas import InventoryItemIn, NormalizedInventoryItem


class ValidationError(Exception):
    pass


def normalize_payload(item: InventoryItemIn) -> NormalizedInventoryItem:
    normalized = NormalizedInventoryItem(**item.model_dump())
    if normalized.action == 'delete' and normalized.quantity != 0:
        raise ValidationError('delete action requires quantity=0')
    return normalized
