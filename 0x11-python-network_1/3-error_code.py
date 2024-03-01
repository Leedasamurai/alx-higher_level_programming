#!/usr/bin/python3
"""
This script takes a URL as input, sends a request to the URL, and displays the body of the response.
It handles urllib.error.HTTPError exceptions and prints the corresponding error code.
"""
from sys import argv
from urllib.request import Request, urlopen
from urllib.error import HTTPError


if __name__ == "__main__":
    url = argv[1]
    req = Request(url)

    try:
        with urlopen(req) as response:
            print(response.read().decode("ascii"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
