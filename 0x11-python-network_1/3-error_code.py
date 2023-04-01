#!/usr/bin/python3
"""Sends a request to URL and prints it response code"""
import urllib.request as request
import urllib.error as error
import sys


if __name__ == '__main__':
    if len(sys.argv) == 2:
        url = sys.argv[1]
        try:
            with request.urlopen(url) as response:
                print(response.read().decode('utf-8'))
        except error.HTTPError as ex:
            print('Error code: {}'.format(ex.code))
