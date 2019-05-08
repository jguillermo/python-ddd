# -*- coding: utf-8 -*-
from bootstrap.framework import FalconApi
from bootstrap.sqlalchemy import load_mapper_app
from sdk.env import load_env_file

class App:
    def __init__(self):
        #load_env_file('config/config.env')
        load_mapper_app()
        self.api = FalconApi().api
