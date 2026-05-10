from unittest.mock import create_autospec

import pytest
from app_fastapi.app_module import AppModule
from app_fastapi.item_router import ItemRouter
from core.item_service import ItemService


class TestAppModule(AppModule):
    item_service: ItemService
    item_router: ItemRouter

    def __init__(self, item_service: ItemService):
        self.item_service = item_service
        self.item_router = ItemRouter(item_service)


@pytest.fixture(autouse=True)
def mock_item_service() -> ItemService:
    return create_autospec(ItemService)


@pytest.fixture(autouse=True)
def test_app_module(mock_item_service) -> TestAppModule:
    return TestAppModule(item_service=mock_item_service)
