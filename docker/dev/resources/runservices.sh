#!/bin/bash

#xray-daemon -o -b localhost:2000 -n $DEPLOY_REGION &
gunicorn -c /resources/gunicorn.py wsgi:api
