#!/usr/bin/python3
"""
This script fetches the 'X-Request-Id' header value from a URL provided as a command-line argument using urllib.request.
"""

from sys import argv
from urllib.request import Request, urlopen


if __name__ == "__main__":
    url = argv[1]
    req = Request(url)

    with urlopen(req) as response:
        print(dict(response.headers).get("X-Request-Id"))
