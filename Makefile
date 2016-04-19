.PHONY: test
test:
	coverage run --source=see.py -m tests -v
	pyflakes *.py
	pep8 --statistics --count *.py

.PHONY: lint
lint:
	@flake8 *.py && echo OK
