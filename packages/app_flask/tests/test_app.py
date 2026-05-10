from unittest.mock import MagicMock

from fastapi import FastAPI
from fastapi.testclient import TestClient

from app_flask.ItemRouter import ItemRouter
from core.domain import Item
from core.service import ItemService


def _make_client(service: ItemService) -> TestClient:
    router = ItemRouter(service)
    app = FastAPI()
    app.add_api_route("/items/{item_id}", router.get_item, methods=["GET"])
    app.add_api_route("/items", router.create_item, methods=["POST"], status_code=201)
    return TestClient(app)


def test_get_item_found():
    svc = MagicMock(spec=ItemService)
    svc.get_item.return_value = Item(name="widget", id="abc-123")

    resp = _make_client(svc).get("/items/abc-123")

    assert resp.status_code == 200
    assert resp.json() == {"id": "abc-123", "name": "widget"}


def test_get_item_not_found():
    svc = MagicMock(spec=ItemService)
    svc.get_item.return_value = None

    resp = _make_client(svc).get("/items/missing")

    assert resp.status_code == 404


def test_create_item():
    svc = MagicMock(spec=ItemService)
    svc.create_item.return_value = Item(name="new-thing", id="xyz-789")

    resp = _make_client(svc).post("/items", json={"name": "new-thing"})

    assert resp.status_code == 201
    assert resp.json() == {"id": "xyz-789", "name": "new-thing"}
    svc.create_item.assert_called_once_with("new-thing")
