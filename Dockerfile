FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 DJANGO_ALLOW_INSECURE_KEY=1
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN python manage.py collectstatic --no-input
ENV DJANGO_ALLOW_INSECURE_KEY=

EXPOSE 8000
CMD ["sh", "-c", "python manage.py migrate --no-input && python manage.py seed_catalog && gunicorn config.wsgi --bind 0.0.0.0:${PORT:-8000} --workers 3"]
