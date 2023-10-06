SHELL   := /bin/bash
PYTHON  ?= python3

export PYTHONWARNINGS := default

.PHONY: all test lint lint-extra shellcheck clean cleanup

all:

test: lint lint-extra shellcheck

lint:
	flake8 scripts/*.py
	pylint scripts/*.py

lint-extra:
	mypy --strict --disallow-any-unimported scripts/*.py

shellcheck:
	shellcheck scripts/*.sh

clean: cleanup

cleanup:
	find -name '*~' -delete -print
	rm -fr .mypy_cache/
