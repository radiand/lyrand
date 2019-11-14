ut:
	python3 -m unittest --verbose

types:
	mypy *.py

lint:
	flake8 *.py

test: ut types lint
