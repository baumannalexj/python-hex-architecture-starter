from fastapi import FastAPI
from . import container


def create_app() -> FastAPI:
    item_router = container.item_router

    app = FastAPI(title="Hex FastAPI")
    app.add_api_route("/items/{item_id}", item_router.get_item, methods=["GET"])
    app.add_api_route("/items", item_router.create_item, methods=["POST"], status_code=201)

    return app


app = create_app()
