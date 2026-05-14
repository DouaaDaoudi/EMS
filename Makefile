run:
	uvicorn main:app --reload

test:
	pytest

freeze:
	pip freeze > requirements.txt