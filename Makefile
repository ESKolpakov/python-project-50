install:
	poetry install

gendiff:
	poetry run gendiff

build: check
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user dist/*.whl --force-reinstall

test:
	poetry run pytest

lint:
	poetry run flake8 gendiff

test-coverage:
	poetry run pytest --cov=gendiff --cov-report=xml

check: selfcheck test lint

selfcheck:
	poetry check

.PHONY: install gendiff build publish package-install package-reinstall lint test test-coverage selfcheck check