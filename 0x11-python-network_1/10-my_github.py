#!/usr/bin/python3
"""Prints the Github id of a user"""
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) == 3:
        user_url = 'https://api.github.com/user'
        username = sys.argv[1]
        password_token = sys.argv[2]
        headers = {
                'Accept': 'application/vnd.github.v3+json',
                'Username': username,
                'Authorization': 'Bearer {}'.format(password_token),
                }
        response = requests.get(user_url, headers=headers)
        if response.status_code == 200:
            user = response.json()
            if user['login'] == username:
                print(user['id'])
            else:
                print('None')
        else:
            print('None')
