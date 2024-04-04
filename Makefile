install:
	poetry install

install-force:
	python3 -m pip install --user --force-reinstall dist/*.whl

gendiff:
	poetry run python -m gendiff.scripts.gendiff

build:
	poetry build
