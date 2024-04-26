#!/bin/bash
# Display all http methods from server of given url
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
