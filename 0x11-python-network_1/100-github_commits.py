#!/usr/bin/python3
"""
This script list last 10 commits of a given GitHub repo
"""


def main():
    """
    List last 10 commits using GitHub API
    """
    import requests
    from sys import argv

    repo, owner = argv[1], argv[2]
    URL = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    res = requests.get(URL)
    max = 10
    for cmt in res.json():
        print("{}: {}".format(cmt['sha'], cmt['commit']['author']['name']))
        max -= 1
        if max <= 0:
            break


if __name__ == '__main__':
    main()
