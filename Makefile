# Makefile for Anvil Project

.PHONY: help install setup-hooks format lint test up down api

help:
@echo "Commands:"
@echo "  install      : Install python dependencies."
@echo "  setup-hooks  : Install pre-commit hooks."
@echo "  format       : Format code with black and isort."
@echo "  lint         : Lint code with ruff."
@echo "  test         : Run pytest."
@echo "  up           : Start the full dev stack (API, DB, Worker) with Docker."
@echo "  down         : Stop the full dev stack."
@echo "  api          : Run the FastAPI dev server locally (without Docker)."

install:
pip install -e ".[dev]"

setup-hooks:
pre-commit install

format:
black .
isort .

lint:
ruff check .

test:
pytest

up:
docker-compose up -d

down:
docker-compose down

api:
uvicorn anvil_api.main:app --reload
