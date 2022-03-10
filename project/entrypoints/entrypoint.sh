#! /bin/bash

# # Wait for Postgres to be up and slhealthy
# echo "Waiting for postgres..."

# while ! nc -z web-db 5432; do
#   sleep 0.1
# done

# echo "PostgreSQL started"

# exec "$@"

uvicorn api.main:app \
  --host 0.0.0.0 \
  --port="${APP_PORT:-8001}" \
  --workers 1 \
  --reload  \
  "$@";
