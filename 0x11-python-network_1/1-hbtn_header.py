#!/usr/bin/python3
"""
This script takes a URL as input from command line, sends request to the URL,
and displays the value of X-Request-Id variable found in header of response.
"""
from sys import argv
from urllib.request import Request, urlopen


if __name__ == "__main__":
    url = argv[1]
    req = Request(url)

    with urlopen(req) as response:
        print(dict(response.headers).get("X-Request-Id"))
