.PHONY: server

env: requirements.txt
	virtualenv $@
	. $@/bin/activate && pip install --requirement requirements.txt

db.sqlite3: env
	. env/bin/activate && python manage.py migrate

server: db.sqlite3 env
	. env/bin/activate && python manage.py runserver
