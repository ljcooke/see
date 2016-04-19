.PHONY: tests
tests:
	python -m tests

.PHONY: lint
lint:
	@flake8 *.py && echo OK
