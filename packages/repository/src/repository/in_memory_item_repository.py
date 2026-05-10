from core.domain import Item
from core.ports import ItemRepository


class InMemoryItemRepository(ItemRepository):
    def __init__(self) -> None:
        default_item = Item("default item")
        self._store: dict[str, Item] = {default_item.id: default_item}

    def get_by_id(self, item_id: str) -> Item | None:
        return self._store.get(item_id)

    def save(self, item: Item) -> None:
        self._store[item.id] = item
