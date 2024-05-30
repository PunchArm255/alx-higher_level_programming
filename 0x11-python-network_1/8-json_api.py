#!/usr/bin/python3
"""
This script sends POST request to URL with a letter
as parameter
"""


def main():
    """
    Send Post request to URL with variable q &
    display decoded JSON response
    """
    import requests
    from sys import argv

    URL = 'http://0.0.0.0:5000/search_user'
    payload = {}
    payload['q'] = "" if (len(argv) == 1) else argv[1]
    res = requests.post(URL, data=payload)
    try:
        res_json = res.json()
        if not res_json:
            print("No result")
        else:
            print("[{}] {}".format(res_json.get('id'), res_json.get('name')))
    except ValueError:
        print("Not a valid JSON")


if __name__ == '__main__':
    main()
