#!/usr/bin/python3
"""Fetches a URL"""
import urllib.request as req

if __name__ == "__main__":
    with req.urlopen('https://alx-intranet.hbtn.io/status') as r:
        if r.status == 200:
            data = r.read()
            print('Body response:')
            print('\t- type: {}'.format(type(data)))
            print('\t- content: {}'.format(data))
            print('\t- utf8 content: {}'.format(data.decode()))
