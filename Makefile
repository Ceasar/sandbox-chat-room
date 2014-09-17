.PHONY: server

env: requirements.txt
	virtualenv env
	pip install -r requirements.txt

db.sqlite3: env
	source env/bin/activate & python manage.py migrate

server: db.sqlite3 env
	source env/bin/activate & python manage.py runserver
