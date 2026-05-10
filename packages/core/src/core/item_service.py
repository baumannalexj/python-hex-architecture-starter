from dataclasses import dataclass
from .domain import Item
from .ports import ItemRepository, IEventClient


@dataclass
class ItemService:
    item_repository: ItemRepository
    event_client: IEventClient

    def get_item(self, item_id: str) -> Item | None:
        return self.item_repository.get_by_id(item_id)

    def create_item(self, name: str) -> Item:
        item = Item(name=name)
        self.item_repository.save(item)
        self.event_client.publish(item.id, "item.created")
        return item
