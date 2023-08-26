#!/usr/bin/python3
'''A module containing IO functions.
'''
from json import JSONDecoder


def load_from_json_file(filename):
    '''Creates an object from its JSON representation stored in a file.

    Args:
        filename (str): The name of the file containing the JSON string.

    Returns:
        any: An object corresponding to the JSON string in the file,
        otherwise an exception is thrown.
    '''
    lines = []
    with open(filename, encoding='utf-8') as file:
        for line in file.readlines():
            lines.append(line)
    return JSONDecoder().decode(''.join(lines))
