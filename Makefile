.PHONY: test
test:
	coverage run --source=see.py setup.py test
	coverage html
	pyflakes *.py
	pep8 --statistics --count *.py

.PHONY: lint
lint:
	@flake8 *.py && echo OK
