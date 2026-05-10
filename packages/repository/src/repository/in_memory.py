from core.domain import Item
from core.ports import ItemRepository


class InMemoryItemRepository(ItemRepository):
    def __init__(self) -> None:
        self._store: dict[str, Item] = {}

    def get(self, item_id: str) -> Item | None:
        return self._store.get(item_id)

    def save(self, item: Item) -> None:
        self._store[item.id] = item
