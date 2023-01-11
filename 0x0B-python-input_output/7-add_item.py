#!/usr/bin/python3
'''A script that stores arguments to a JSON file.
usage: ./7-add_item.py ......... ....... ..
'''
import sys
import os
from importlib import import_module as using


save_to_json_file, load_from_json_file = (
    using('5-save_to_json_file').save_to_json_file,
    using('6-load_from_json_file').load_from_json_file
)
'''The functions for saving and loading lists.
'''
args_list = []
'''The list of arguments.
'''
args_list_file_name = 'add_item.json'
'''The file name of the file containing the list of arguments.
'''


def run():
    '''Runs the routines of this script.
    '''
    if not os.path.exists(args_list_file_name):
        with open(args_list_file_name, mode='w', encoding='utf-8') as file:
            file.write('[]')
    json_list = load_from_json_file(args_list_file_name)
    if (type(json_list) is list) and all(type(s) is str for s in json_list):
        args_list.extend(json_list)
    args_list.extend(sys.argv[1:])
    save_to_json_file(args_list, args_list_file_name)


if __name__ == '__main__':
    run()
