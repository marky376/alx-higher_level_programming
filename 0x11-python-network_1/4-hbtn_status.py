#!/usr/bin/python3
"""What's my status? #1"""

import requests

if __name__ == "__main__":
    """
    Python script that fetches https://alx-intranet.hbtn.io/status
    """
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
