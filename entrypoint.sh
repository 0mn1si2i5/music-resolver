#!/bin/bash
set -e

echo "Starting music resolver..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8788 --workers ${UVICORN_WORKERS:-1}
