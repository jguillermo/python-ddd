#!/bin/bash

#nosetests --with-coverage --with-xunit -v /app/tests/unit/suite_test.py
nosetests --cover-branches --with-coverage --cover-erase --cover-html --cover-package=src.user.application --with-xunit -v /app/tests/unit/suite_test.py
