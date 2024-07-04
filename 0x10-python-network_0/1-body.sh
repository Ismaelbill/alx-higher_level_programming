#!/bin/bash
# script that takes in a URL, sends a GET request to the URL, and displays the body of the response
status=$(curl -i -s -X GET $(1) | head -n 1 | cut -d " " -f2)

if [ $status -eq 200 ]; then
	curl -i -s -X GET $1
fi
