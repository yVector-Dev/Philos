#!/usr/bin/env bash
# Build step for Render / Railway / any buildpack host.
set -o errexit
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate --no-input
python manage.py seed_catalog
