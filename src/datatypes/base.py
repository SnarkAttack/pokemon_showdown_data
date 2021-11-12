import abc
import json

class BaseDataType(abc.ABC):

    def __init__(self):
        self._db_file = 'pokeshowdata.db'

    def convert_to_json(self):
        return vars(self)