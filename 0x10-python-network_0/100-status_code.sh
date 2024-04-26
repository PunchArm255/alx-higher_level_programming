#!/bin/bash
# Sends get request to given url and displays response status code
curl -s -o /dev/null -w "%{http_code}" "$1"
