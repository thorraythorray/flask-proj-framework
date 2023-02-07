#!/bin/bash
DATA_PATH=/data
LOG_PATH=/var/log/apps
PWD=$(cd $(dirname $0); pwd)

if [ ! -d $DATA_PATH ]; then
    mkdir -p $DATA_PATH
fi

if [ ! -d $LOG_PATH ]; then
    mkdir -p $LOG_PATH
fi

apt-get install python3-dev default-libmysqlclient-dev build-essential supervisor
cp ./misc/config/supervisor_pyfla.conf /etc/supervisor/conf.d/
supervisorctl reload
docker compose -f ./docker-compose.yml up -d