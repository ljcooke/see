.PHONY: lint
lint:
	@flake8 *.py && echo OK
