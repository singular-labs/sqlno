import importlib


class Engine(object):
    ATHENA = importlib.import_module('sqlno.athena.engine')
    MYSQL = importlib.import_module('sqlno.common.engine')
