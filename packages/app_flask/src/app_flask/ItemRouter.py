from fastapi import HTTPException
from pydantic import BaseModel

from core.service import ItemService


class CreateItemRequest(BaseModel):
    name: str


class ItemRouter:
    def __init__(self, item_service: ItemService) -> None:
        self._item_service = item_service

    def get_item(self, item_id: str):
        item = self._item_service.get_item(item_id)
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return {"id": item.id, "name": item.name}

    def create_item(self, body: CreateItemRequest):
        item = self._item_service.create_item(body.name)
        return {"id": item.id, "name": item.name}
