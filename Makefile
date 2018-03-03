#
# Pylint Quotes
#

PKG_VER := $(shell cat pylint_quotes/__version__.py | grep __version__ | awk '{print $$3}' | tr -d "'")


.PHONY: init
init: ## Initialize the repo for development
	pip install pipenv
	pipenv install --dev --skip-lock

.PHONY: coverage
coverage: ## Run tests and report on coverage
	pipenv run py.test --cov-report term --cov=pylint_quotes tests

.PHONY: lint
lint: ## Lint the source code (pylint, flake8, isort)
	pipenv run pylint pylint_quotes
	pipenv run flake8 --ignore E501 pylint_quotes
	pipenv run isort pylint_quotes -rc -c --diff

.PHONY: publish
publish: ## Publish to PyPi
	pip install 'twine>=1.5.0'
	python setup.py sdist bdist_wheel
	twine upload dist/*
	rm -rf build dist .egg pylint_quotes.egg-info

.PHONY: test
test: ## Run unit tests
	pipenv run py.test

.PHONY: version
version: ## Print the version of Synse Server
	@echo "$(PKG_VER)"

.PHONY: help
help:  ## Print Make usage information
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

.DEFAULT_GOAL := help