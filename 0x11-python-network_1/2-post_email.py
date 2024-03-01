#!/usr/bin/python3
"""
This script takes in a URL and an email from the command line, sends a POST request to the URL
with the email as a parameter, and displays the body of the response.
"""
from sys import argv
from urllib.parse import urlencode
from urllib.request import Request, urlopen


if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}
    data = urlencode(value).encode("ascii")
    req = Request(url, data)

    with urlopen(req) as response:
        print(response.read().decode("utf-8", "replace"))
