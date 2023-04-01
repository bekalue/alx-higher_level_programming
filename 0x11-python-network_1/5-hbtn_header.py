#!/usr/bin/python3
"""Fetches a header of a response from URL."""
import sys
import requests


if __name__ == '__main__':
    if len(sys.argv) == 2:
        response = requests.get(sys.argv[1])
        if 'X-Request-Id' in response.headers:
            print(response.headers['X-Request-Id'])
