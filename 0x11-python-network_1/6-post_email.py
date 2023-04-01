#!/usr/bin/python3
"""Posts an email to url server"""
import sys
import requests


if __name__ == '__main__':
    if len(sys.argv) == 3:
        data = {'email': sys.argv[2]}
        response = requests.post(sys.argv[1], data=data)
        print(response.text)
