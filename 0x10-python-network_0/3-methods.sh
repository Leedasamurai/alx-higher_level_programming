#!/bin/bash
# script to get the allowed methods in server if availaible OPTIONS http request
curl -s -I -X OPTIONS "$1" | grep 'Allow:' | cut -f2- -d' '
