# variables
SDK := moex_python_sdk

# for api docs
SOURCE := ./docs/source/
MODULES := ./docs/source/_modules/
BUILD_DIR := ./docs/build/


init:
	poetry install && poetry update

.PHONY: test
test:
	poetry run pytest -n 8

build:
	poetry build


new.docs:
	poetry run sphinx-quickstart ${SOURCE}

.PHONY: docs
docs:
	poetry run sphinx-apidoc -M -o ${MODULES} ${SDK}
	poetry run sphinx-build -M html ${SOURCE} ${BUILD_DIR}
