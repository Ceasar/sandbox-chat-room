.PHONY: server shell test

# Either "development" or "production".
#
# - Use "development" on your development computer as you interact manually with
#   the application
#
# - Use "production" when you deploy your application for the world to use
#
ENV = development

export DATABASE_URL = sqlite:///db.sqlite3

env: requirements.txt
	virtualenv $@
	. $@/bin/activate && pip install --requirement requirements.txt

db.sqlite3: env
	. env/bin/activate && python manage.py migrate

server: db.sqlite3 env
ifeq ($(ENV), production)
	. env/bin/activate && gunicorn chatroom.wsgi --log-file -
else
	. env/bin/activate && python manage.py runserver
endif

shell:
	bash --rcfile env/bin/activate; exit

test: env
	. env/bin/activate && python manage.py test
