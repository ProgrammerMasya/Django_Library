#!/bin/bash
set -ex

until nc -w 1 -z db 5432; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done
>&2 echo "Postgres is up - executing command"

python3 manage.py migrate --noinput

python3 manage.py collectstatic --noinput

python3 manage.py runserver 0.0.0.0:8000
