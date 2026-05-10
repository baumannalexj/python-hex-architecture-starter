# python-hex-architecture-starter
Starter FastAPI app built with manual dependency injection (no framework) and hexagonal architecture.

## Structure

```
packages/
├── core/          # business logic, ports (interfaces), no external dependencies
├── repository/    # in-memory repository adapter
├── clients/       # AWS SNS event client adapter
└── app_flask/     # FastAPI app, composition root (app_fastapi module)
```

## Setup

```bash
uv sync --all-packages --all-groups
```

## Run

```bash
uv run uvicorn app_fastapi.main:create_app --factory --reload
```

## Test

```bash
uv run pytest packages/core/tests packages/repository/tests packages/clients/tests packages/app_flask/tests -v
```
