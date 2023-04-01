#!/usr/bin/python3
"""Sends a search parameter to a URL."""
import requests
import sys


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    query = sys.argv[1] if len(sys.argv) == 2 else ""
    data = {'q': query}
    response = requests.post(url, data=data)
    try:
        to_json = response.json()
        if to_json:
            print('[{}] {}'.format(to_json['id'], to_json['name']))
        else:
            print('No result')
    except Exception:
        print('Not a valid JSON')
