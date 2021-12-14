
web: gunicorn -b 127.0.0.1:8001 whipp.wsgi:application
release python manage.py   makemigrations --noinput
release python manage.py   migrate --noinput
