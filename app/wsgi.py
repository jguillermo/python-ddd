# -*- coding: utf-8 -*-
import gc
from bootstrap.app import App

gc.collect()
api = App().api
