#!/usr/bin/python3
"""Sends a request to a URL and prints its response code."""
import sys
import requests


if __name__ == '__main__':
    if len(sys.argv) == 2:
        response = requests.get(sys.argv[1])
        if response.status_code >= 400:
            print('Error code: {}'.format(response.status_code))
        else:
            print(response.text)
