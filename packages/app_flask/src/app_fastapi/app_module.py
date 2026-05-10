from abc import ABC

from clients.aws_sns import AwsSnsClient
from core.item_service import ItemService
from repository.in_memory_item_repository import InMemoryItemRepository
from .config import Settings
from .item_router import ItemRouter


class AppModule(ABC):
    """shared with TestAppModule"""

    item_router: ItemRouter


class FastApiAppModule(AppModule):
    def __init__(self) -> None:
        item_repository = InMemoryItemRepository()
        event_client = AwsSnsClient(
            topic_arn=Settings().sns_topic_arn,
            region=Settings().aws_region,
        )
        item_service = ItemService(
            _item_repository=item_repository, _event_client=event_client
        )

        self.item_router = ItemRouter(item_service)
