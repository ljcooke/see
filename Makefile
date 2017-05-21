.PHONY: test
test:
	python2 setup.py test
	python3 setup.py test

.PHONY: coverage
coverage:
	coverage run --source=see setup.py test
	coverage report
	coverage html
	flake8 see

.PHONY: lint
lint:
	flake8 see
	pylint see

.PHONY: clean
clean:
	rm -rf build
	rm -rf ./*.pyc see/*.pyc __pycache__ see/__pycache__
	rm -rf .eggs *.egg-info
	(cd docs && make clean)

.PHONY: docs
docs:
	(cd docs && make html)

.PHONY: dist
dist:
	python3 setup.py sdist bdist_wheel

.PHONY: publish
publish:
	python3 setup.py sdist bdist_wheel upload # -r testpypi
