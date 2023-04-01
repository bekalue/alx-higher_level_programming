#!/usr/bin/python3
"""lists 10 commits (from the most recent to oldest) of the repository"""
import sys
import requests


if __name__ == '__main__':
    if len(sys.argv) == 3:
        repository = sys.argv[1]
        owner_name = sys.argv[2]
        url = 'https://api.github.com/repos/{}/{}/commits?{}'.format(
                owner_name,
                repository,
                'per_page=10')
        header = {'Accept': 'application/vnd.github+json'}
        response = requests.get(url, headers=header)
        if response.status_code == 200:
            commits = response.json()
            for commit in commits:
                print('{}: {}'.format(
                    commit['sha'],
                    commit['commit']['author']['name']))
