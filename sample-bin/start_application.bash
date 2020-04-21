#!/bin/bash

NAME="app"
PROJECT_DIR="/home/deepak/vendor-web"
PROJECT_SRC="$PROJECT_DIR/app"
SOCKFILE="$PROJECT_DIR/gunicorn.sock"
LOGFILE="$PROJECT_DIR/logs/gunicorn.log"

USER=`whoami`
GROUP=`id -g -n`
NUM_WORKERS=3

DJANGO_SETTINGS_MODULE=app.settings
DJANGO_WSGI_MODULE=app.wsgi

cd $PROJECT_SRC

source /home/deepak/vendor-web/venv/bin/activate

export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$PROJECT_SRC:$PYTHONPATH

echo "Starting $NAME"

#python admin_web/generator.py

exec gunicorn -b 127.0.0.1:8989 ${DJANGO_WSGI_MODULE}:application \
 --name $NAME \
 --workers $NUM_WORKERS \
 --user=$USER --group=$GROUP \
 --bind=unix:$SOCKFILE \
 --log-level=info \
 --timeout 300 \
 --log-file=-