.PHONY: server

db.sqlite3:
	python manage.py migrate

server: db.sqlite3
	python manage.py runserver
