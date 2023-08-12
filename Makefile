# variables
SDK := moex_python_sdk

# for api docs
SOURCE := ./docs/source/
MODULES := ./docs/source/modules/
BUILD_DIR := ./docs/build/


init:
	poetry install && poetry update

.PHONY: test
test:
	poetry run pytest -s

build:
	poetry build


.PHONY: docs
docs:
	poetry run sphinx-apidoc -M -o ${MODULES} ${SDK}
	poetry run sphinx-build -M html ${SOURCE} ${BUILD_DIR}
