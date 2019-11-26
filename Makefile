CODE = maru tests
PYTHON = poetry run

.PHONY: pretty lint test

pretty:
	$(PYTHON) black --target-version py36 --skip-string-normalization $(CODE)
	$(PYTHON) isort --apply --recursive $(CODE)
	$(PYTHON) unify --in-place --recursive $(CODE)

lint:
	$(PYTHON) black --target-version py36 --check --skip-string-normalization $(CODE)
	$(PYTHON) flake8 --jobs 4 --statistics $(CODE)
	$(PYTHON) pylint --jobs 4 --rcfile=setup.cfg $(CODE)
	$(PYTHON) mypy $(CODE)

test:
	$(PYTHON) pytest -n 8 --boxed tests

coverage:
	$(PYTHON) pytest --cov=maru
	$(PYTHON) codecov
