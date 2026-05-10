from unittest.mock import create_autospec

import pytest
from core.domain import Item
from core.item_service import ItemService
from core.ports import ItemRepository, IEventClient


@pytest.fixture(autouse=True)
def mock_item_repository():
    return create_autospec(ItemRepository)


@pytest.fixture(autouse=True)
def mock_event_client():
    return create_autospec(IEventClient)


@pytest.fixture(autouse=True)
def item_service(mock_item_repository, mock_event_client):
    return ItemService(
        _item_repository=mock_item_repository, _event_client=mock_event_client
    )


def test_get_item_delegates_to_repo(item_service, mock_item_repository):
    expected = Item(name="foo", id="123")
    mock_item_repository.get_by_id.return_value = expected

    result = item_service.get_item("123")

    assert result == expected
    mock_item_repository.get_by_id.assert_called_once_with("123")


def test_get_item_returns_none_when_missing(item_service, mock_item_repository):
    mock_item_repository.get_by_id.return_value = None

    assert item_service.get_item("missing") is None


def test_create_item_saves_and_publishes(
    item_service, mock_item_repository, mock_event_client
):
    item = item_service.create_item("widget")

    assert item.name == "widget"
    mock_item_repository.save.assert_called_once_with(item)
    mock_event_client.publish.assert_called_once_with(item.id, "item.created")
