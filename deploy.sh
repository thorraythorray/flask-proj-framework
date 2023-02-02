#!/bin/bash
DATA_PATH=/data
LOG_PATH=/var/log/apps

if [ ! -d $DATA_PATH ]; then
    mkdir -p $DATA_PATH
fi

if [ ! -d $LOG_PATH ]; then
    mkdir -p $LOG_PATH
fi

apt-get install python3-dev default-libmysqlclient-dev build-essential