install:
	uv sync

build:
	uv build

lint:
	uv run ruff check .

help:
	uv run gendiff -h