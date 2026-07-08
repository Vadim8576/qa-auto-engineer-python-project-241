install:
	uv sync

build:
	uv build

lint:
	uv run ruff check .

run:
	uv run gendiff -h