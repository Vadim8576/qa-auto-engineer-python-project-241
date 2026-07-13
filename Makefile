install:
	uv sync

build:
	uv build

lint:
	uv run ruff check .

fix:
	uv run ruff check --fix

help:
	uv run gendiff -h

test:
	uv run pytest

test-coverage:
	uv run pytest --cov

check: test lint test-coverage