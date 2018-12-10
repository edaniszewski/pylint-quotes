#
# Pylint Quotes
#

PKG_VER := $(shell python setup.py --version)


.PHONY: deps
deps: ## Update the frozen pip dependencies (requirements.txt)
	tox -e deps

.PHONY: lint
lint: ## Lint the source code (pylint, flake8, isort)
	tox -e lint

.PHONY: publish
publish: ## Publish to PyPi
	tox -e publish

.PHONY: test
test: ## Run unit tests
	tox

.PHONY: version
version: ## Print the version of Synse Server
	@echo "$(PKG_VER)"

.PHONY: help
help:  ## Print Make usage information
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

.DEFAULT_GOAL := help