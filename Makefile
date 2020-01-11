ut:
	python3 -m unittest --verbose

types:
	mypy lyrand

lint:
	flake8 *.py

test: ut types lint
