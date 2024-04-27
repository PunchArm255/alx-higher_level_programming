#!/usr/bin/python3
"""
This script send POST request to given URL
(using 'requests' pckge)
"""


def main():
    """
    Send POST request to URL with email parameter &
    display response body (using 'requests' pkg)
    """
    import requests
    from sys import argv

    URL, email = argv[1], argv[2]
    res = requests.post(URL, data={'email': email})
    print(res.text)


if __name__ == '__main__':
    main()
