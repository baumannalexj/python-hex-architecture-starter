from fastapi import FastAPI
from .app_module import AppModule


def create_app(app_module: AppModule) -> FastAPI:
    item_router = app_module.item_router

    app = FastAPI(title="Hex FastAPI")
    app.add_api_route("/items/{item_id}", item_router.get_item, methods=["GET"])
    app.add_api_route(
        "/items", item_router.create_item, methods=["POST"], status_code=201
    )

    return app
