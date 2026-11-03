# Пример Makefile. В проекте файл должен лежать в корне

.PHONY: init sync test lint format typecheck check

init:
	uv sync && \
	uv run pre-commit install

sync:  # приводит окружение в соответствие с pyproject.toml и uv.lock
	uv sync --all-groups

test:
	uv run --group test pytest

lint:
	uv run ruff check --fix .

format:
	uv run isort .
	uv run black .

typecheck:
	uv run mypy src/

check:
	uv run ruff check .
	uv run isort --check-only .
	uv run black --check .
	uv run mypy src/
	uv run --group test pytest
