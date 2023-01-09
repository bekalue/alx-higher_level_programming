#!/usr/bin/python3
'''A module for manipulating objects.
'''


def add_attribute(obj, attribute, value):
    '''Tries to add a new attribute to an object if possible.

    Args:
        obj (any): The object to modify.
        name (str): The name of the attribute.
        value (any): The value of the attribute.
    '''
    if '__dict__' in dir(obj) and type(obj.__dict__) is dict:
        obj.__dict__[attribute] = value
    else:
        raise TypeError("can't add new attribute")
