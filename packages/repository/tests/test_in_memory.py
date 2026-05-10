from repository.in_memory import InMemoryItemRepository
from core.domain import Item


def test_save_and_get():
    repo = InMemoryItemRepository()
    item = Item(name="test", id="1")
    repo.save(item)
    assert repo.get("1") == item


def test_get_missing_returns_none():
    repo = InMemoryItemRepository()
    assert repo.get("nonexistent") is None


def test_save_overwrites():
    repo = InMemoryItemRepository()
    repo.save(Item(name="original", id="1"))
    repo.save(Item(name="updated", id="1"))
    assert repo.get("1").name == "updated"
