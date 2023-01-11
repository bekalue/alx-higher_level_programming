#!/usr/bin/python3
'''A module containing IO functions.
'''


def append_after(filename="", search_string="", new_string=""):
    '''Inserts a line of text to a file, after each line containing
    a specific string.

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The string to look for in each line.
        new_string (str): The string to add on the next line after a
        match is found in the previous line.
    '''
    res = []
    with open(filename, mode='r') as file:
        for line in file.readlines():
            res.append(line)
            if line.find(search_string) >= 0:
                res.append(new_string)
    with open(filename, mode='w') as file:
        file.writelines(res)
