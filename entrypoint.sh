#!/usr/bin/env bash

cd /pythonbackenddemo
gunicorn --workers=3 --threads=3 api:app
