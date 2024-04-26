#!/usr/bin/python3

"""
This script sends a request to a URL and displays the response body. 
If an HTTP error occurs, it prints the error code.
"""

import urllib.error
import urllib.request
import sys

if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as resp:
            print(resp.read().decode('UTF-8'))
    except error.HTTPError as er:
        print('Error code:', er.code)
