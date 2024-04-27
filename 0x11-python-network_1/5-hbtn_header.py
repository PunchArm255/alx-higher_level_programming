#!/usr/bin/python3
"""X-Request-Id header variable of request to URL
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
