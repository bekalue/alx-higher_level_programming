#!/usr/bin/python3
"""
A module that conatins a function which prints a string
to standard output.
"""


def say_my_name(first_name, last_name=""):
    """
    A function that prints a string which is
    `My name is <first name> <last name>` to standard output.

    Args:
        first_name (str): a parameter for the first name.
        last_name (str): a paramer for the last name.

    Raises:
        TypeError: if first name and last name are not strings.

    """

    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    elif not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    else:
        print(f'My name is {first_name} {last_name}')
