#!/usr/bin/python3
'''A module containing IO functions.
'''


def class_to_json(obj):
    '''Retrieves the dictionary description of an object.

    Args:
        obj (any): An object whose attributes are to be retrieved.

    Returns:
        dict: The attributes of the object, otherwise None.
    '''
    if '__dict__' in dir(obj):
        return obj.__dict__
