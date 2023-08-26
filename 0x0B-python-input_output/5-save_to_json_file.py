#!/usr/bin/python3
"""
A module containing IO functions for a file.
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Saves the JSON representation of an object to a file.

    Args:
        my_obj (any): An object to convert to JSON.
        filename (str): The file to save the JSON string in.
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)
