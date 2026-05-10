import pytest
from fastapi.testclient import TestClient

from app_fastapi.main import create_app
from core.domain import Item


@pytest.fixture(autouse=True)
def test_client(test_app_module):
    return TestClient(create_app(test_app_module))


def test_get_item_found(test_client, mock_item_service):

    mock_item_service.get_item.return_value = Item(name="widget", id="abc-123")

    resp = test_client.get("/items/abc-123")

    assert resp.status_code == 200
    assert resp.json() == {"id": "abc-123", "name": "widget"}


def test_get_item_not_found(test_client, mock_item_service):
    mock_item_service.get_item.return_value = None

    resp = test_client.get("/items/missing")

    assert resp.status_code == 404


def test_create_item(test_client, mock_item_service):
    mock_item_service.create_item.return_value = Item(name="new-thing", id="xyz-789")

    resp = test_client.post("/items", json={"name": "new-thing"})

    assert resp.status_code == 201
    assert resp.json() == {"id": "xyz-789", "name": "new-thing"}
    mock_item_service.create_item.assert_called_once_with("new-thing")
