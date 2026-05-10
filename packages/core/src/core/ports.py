from abc import ABC, abstractmethod
from .domain import Item


class ItemRepository(ABC):
    @abstractmethod
    def get(self, item_id: str) -> Item | None: ...

    @abstractmethod
    def save(self, item: Item) -> None: ...


class EventClient(ABC):
    @abstractmethod
    def publish(self, item_id: str, event_type: str) -> None: ...
