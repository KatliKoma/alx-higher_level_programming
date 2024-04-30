#!/usr/bin/python3
"""
This script fetches the 'X-Request-Id' header value from a URL provided as a command-line argument using urllib.request.
"""

from urllib import request
from sys import argv

if __name__ == "__main__":
    with request.urlopen(argv[1]) as page:
        print(page.getheader("X-Request-Id"))
