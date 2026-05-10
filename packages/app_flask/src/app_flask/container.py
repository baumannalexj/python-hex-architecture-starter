from core.service import ItemService
from repository.in_memory import InMemoryItemRepository
from clients.aws_sns import AwsSnsClient
from .ItemRouter import ItemRouter
from .config import Settings


def provides_item_service(settings: Settings) -> ItemService:
    repo = InMemoryItemRepository()
    event_client = AwsSnsClient(
        topic_arn=settings.sns_topic_arn,
        region=settings.aws_region,
    )
    return ItemService(item_repository=repo, event_client=event_client)

item_service = provides_item_service(Settings())

item_router = ItemRouter(item_service)
