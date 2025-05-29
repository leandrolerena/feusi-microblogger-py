typeCheck:
	poetry run mypy ./app
	poetry run pylint ./app