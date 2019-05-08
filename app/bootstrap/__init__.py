# -*- coding: utf-8 -*-
import yaml
import json
import codecs


class File:

    @staticmethod
    def read(file):
        return codecs.open(file, 'r', 'utf-8')

    @staticmethod
    def read_yml(file):
        file_object = open(file, 'r')
        return yaml.load(file_object)

    @staticmethod
    def read_json(file):
        file_object = open(file, 'r')
        return json.load(file_object)
