install:
        poetry install

install-force:
        python3 -m pip install --user --force-reinstall dist/*.whl

gendiff:
        poetry run python -m gendiff.scripts.gendiff

build: check
        poetry build

lint:
        flake8 gendiff
        isort --check-only --diff gendiff

selfcheck:
        poetry check

check: selfcheck lint test

.PHONY: install test lint selfcheck check build