#!/usr/bin/python3
"""
This script displays GitHub ID shenanigans
"""


def main():
    """
    Takes GitHub credentials & displays user ID
    """
    import requests
    from sys import argv

    URL = 'https://api.github.com/user'
    username, token = argv[1], argv[2]
    res = requests.get(URL, auth=(username, token))
    print(res.json().get('id'))


if __name__ == '__main__':
    main()
