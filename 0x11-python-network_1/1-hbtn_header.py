#!/usr/bin/python3

"""Response header value #0"""


import urllib.request
import sys

if __name__ == "__main__":
    """
    Python script that takes in a URL,
    sends a request to the URL and displays the value of the
    X-Request-Id variable found in the header of the response
    """
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        id_request = response.getheader('X-Request-Id')
    print(id_request)
