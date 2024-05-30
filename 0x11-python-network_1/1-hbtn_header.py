#!/usr/bin/python3
"""This scripty
- takes url,
- sends request to url and displays the value
- of the X-Request-Id variable in response header
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
