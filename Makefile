.PHONY: test
test:
	python2 setup.py test
	python3 setup.py test

.PHONY: coverage
coverage:
	coverage run --source=see setup.py test
	coverage html
	pyflakes *.py
	pep8 --statistics --count *.py

.PHONY: lint
lint:
	@flake8 *.py && echo OK

.PHONY: clean
clean:
	rm -vrf build ./*.pyc see/*.pyc __pycache__ see/__pycache__ .eggs

.PHONY: dist
dist:
	python setup.py sdist --formats=bztar,gztar,zip
