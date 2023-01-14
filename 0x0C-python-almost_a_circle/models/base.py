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

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        Saves a list of polygons to a file in JSON format.

        Args:
            list_objs (list): A list of polygons.
        '''

        filename = '{}.json'.format(cls.__name__)
        dict_list = []
        if list_objs is not None:
            for obj in list_objs:
                if type(obj) is cls:
                    dict_list.append(obj.to_dictionary())
        with open(filename, mode='w', encoding='utf-8') as f:
            json.dump(dict_list, f)

    @staticmethod
    def from_json_string(json_string):
        '''
        Creates a list from its JSON representation.
        Args:
            json_string (str): A JSON string representation of a list.
        Returns:
            list: A JSON representation of the list of dictionaries.
        '''
        if json_string is None or len(json_string.strip()) == 0:
            return []
        return json.loads(json_string)
