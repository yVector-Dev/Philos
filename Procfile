release: python manage.py migrate --no-input && python manage.py seed_catalog
web: gunicorn config.wsgi --workers 3 --log-file -
