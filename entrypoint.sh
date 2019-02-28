#!/usr/bin/env bash

gunicorn --workers=3 --threads=3 api:app
