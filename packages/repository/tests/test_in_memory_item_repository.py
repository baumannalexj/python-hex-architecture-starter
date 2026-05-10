import pytest
from repository.in_memory_item_repository import InMemoryItemRepository
from core.domain import Item


@pytest.fixture(autouse=True)
def item_repository():
    return InMemoryItemRepository()


def test_save_and_get(item_repository):
    item = Item(name="test", id="1")
    item_repository.save(item)
    assert item_repository.get_by_id("1") == item


def test_get_missing_returns_none(item_repository):
    assert item_repository.get_by_id("nonexistent") is None


def test_save_overwrites(item_repository):
    item_repository.save(Item(name="original", id="1"))
    item_repository.save(Item(name="updated", id="1"))

    item = item_repository.get_by_id("1")
    assert item is not None
    assert item.name == "updated"
    assert item.id == "1"
