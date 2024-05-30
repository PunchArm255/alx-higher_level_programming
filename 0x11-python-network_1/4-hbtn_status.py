#!/usr/bin/python3
"""
This script fetches a URL with 'requests' package
"""


def main():
    """
    Fetch URL 'https://alx-intranet.hbtn.io/status' &
    display body
    """
    import requests

    res = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print("\t- type: {}".format(type(res.text)))
    print("\t- content: {}".format(res.text))


if __name__ == '__main__':
    main()
