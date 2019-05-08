# -*- coding: utf-8 -*-
import logging


class ConsoleLogger(object):

    def __init__(self):
        try:
            self.output = logging
            self.output.basicConfig(
                    format='%(asctime)s [%(levelname)s] - %(name)s - %(message)s',
                    datefmt='[%Y/%m/%d %I:%M:%S %p]'
            )
        except Exception as e:
            raise e
