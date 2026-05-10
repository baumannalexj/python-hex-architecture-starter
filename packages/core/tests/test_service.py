from unittest.mock import MagicMock
from core.domain import Item
from core.service import ItemService


def _make_service():
    repo = MagicMock()
    client = MagicMock()
    return ItemService(repo, client), repo, client


def test_get_item_delegates_to_repo():
    svc, repo, _ = _make_service()
    expected = Item(name="foo", id="123")
    repo.get.return_value = expected

    result = svc.get_item("123")

    assert result == expected
    repo.get.assert_called_once_with("123")


def test_get_item_returns_none_when_missing():
    svc, repo, _ = _make_service()
    repo.get.return_value = None

    assert svc.get_item("missing") is None


def test_create_item_saves_and_publishes():
    svc, repo, client = _make_service()

    item = svc.create_item("widget")

    assert item.name == "widget"
    repo.save.assert_called_once_with(item)
    client.publish.assert_called_once_with(item.id, "item.created")
