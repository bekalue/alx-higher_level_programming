#!/usr/bin/python3
"""sends a request to the url and displays a variable value"""
import sys
import urllib.request as req


if __name__ == '__main__':
    if len(sys.argv) == 1:
        url = sys.argv[1]
        with req.urlopen(url) as response:
            print(response.headers['X-Request-Id'])
