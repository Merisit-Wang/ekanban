#!/bin/bash

set -e
touch /mnt/gunicorn.log
touch /mnt/gunicorn.err
touch /mnt/access.log

# Start Gunicorn processes
echo Starting Gunicorn...
exec gunicorn manager:app \
        --bind 0.0.0.0:5000 \
        --workers 4 \
        --log-level=info \
        --log-file=/mnt/gunicorn.log \
        --access-logfile=/mnt/access.log \
        "$@"
echo Gunicorn is running...