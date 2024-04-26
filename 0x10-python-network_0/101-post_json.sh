#!/bin/bash
# Sends json post request to given url with given json
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
