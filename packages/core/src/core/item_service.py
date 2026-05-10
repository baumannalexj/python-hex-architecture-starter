from dataclasses import dataclass
from .domain import Item
from .ports import ItemRepository, IEventClient


@dataclass
class ItemService:
    _item_repository: ItemRepository
    _event_client: IEventClient

    def get_item(self, item_id: str) -> Item | None:
        return self._item_repository.get_by_id(item_id)

    def create_item(self, name: str) -> Item:
        item = Item(name=name)
        self._item_repository.save(item)
        self._event_client.publish(item.id, "item.created")
        return item
