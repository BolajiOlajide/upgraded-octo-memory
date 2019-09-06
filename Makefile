start_fast:
	uvicorn server.main:app --reload

start_flask:
	python server/flask_main.py
