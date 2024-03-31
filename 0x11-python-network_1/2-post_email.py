#!/usr/bin/python3
"""POST an email #0"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    """
    Python script that takes in a URL and an email,
    sends a POST request to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8)
    """
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode()

    request = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))
