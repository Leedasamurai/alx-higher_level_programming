#!/bin/bash
# Checks if the HTTP status code is 200 and displays the body of the response.

if [ "$(curl -L -s -o /dev/null -w "%{http_code}" "$1")" = "200" ]; then
    curl -Ls "$1"
fi
