#!/usr/bin/python3
"""
A module that contains a text_indentation function.
"""
def text_indentation(text):
    """
    Prints a text with 2 new lines after each of
    these characters: '.', '?' and ':'

    Args:
        text (str): The text to print.
    Raises:
        TypeError: If the text is not a string.

    """

    indentation_characters = [',', '?', ':']
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    else:
        res = []
        print(''.join(res), end='')
