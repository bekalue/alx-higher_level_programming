#!/usr/bin/python3
"""Posts an email to URL server"""
import urllib.request as request
import sys
import urllib.parse as parse


if __name__ == '__main__':
    if len(sys.argv) == 3:
        url = sys.argv[1]
        data = {'email': sys.argv[2]}
        data = bytes(parse.urlencode(data), 'utf-8')
        with request.urlopen(url, data=data) as response:
            print(response.read().decode('utf-8'))
