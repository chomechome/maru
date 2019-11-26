CODE = maru tests

.PHONY: pretty lint test

pretty:
	black --target-version py36 --skip-string-normalization $(CODE)
	isort --apply --recursive $(CODE)
	unify --in-place --recursive $(CODE)

lint:
	black --target-version py36 --check --skip-string-normalization $(CODE)
	flake8 --jobs 4 --statistics $(CODE)
	pylint --jobs 4 --rcfile=setup.cfg $(CODE)
	mypy $(CODE)

test:
	pytest -n 8 --boxed tests

coverage:
	pytest --cov=maru
	codecov
