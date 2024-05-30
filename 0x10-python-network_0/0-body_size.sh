#!/bin/bash
# Get byte size of HTTP response header for given URL.
curl -s "$1" | wc -c
