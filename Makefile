install:
		poetry install

install-force:
		python3 -m pip install --user --force-reinstall dist/*.whl

gendiff:
		poetry run python -m gendiff.scripts.gendiff

build:
		poetry build

lint:
		flake8 gendiff
		isort --check-only --diff gendiff

selfcheck:
		poetry check

check: selfcheck test lint

build: check
		poetry build

.PHONY: install test lint selfcheck check build