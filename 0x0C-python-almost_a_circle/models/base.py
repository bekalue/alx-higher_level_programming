#!/usr/bin/python3
'''Contains classes for working with Polygons.
'''


import json


class Base:
    '''
    Represents the base class for all polygon objects.
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        '''
        Initializes a new polygon object with the given id.
        Args:
            id (int): The id of this polygon object.
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        Creates the JSON representation of a list of dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.
        Returns:
            str: A JSON representation of the list of dictionaries.
        '''

        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
