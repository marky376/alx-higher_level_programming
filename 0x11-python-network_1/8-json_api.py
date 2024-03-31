#!/usr/bin/python3
"""8. Search API"""

import requests
import sys
"""
Python script that takes in a letter and sends a
POST request to http://0.0.0.0:5000/search_user with the letter as a paramet
"""
if __name__ == "__main__":
    try:
        url = "http://0.0.0.0:5000/search_user"
        if len(sys.argv) < 2:
            q = ""
        else:
            q = sys.argv[1]

        response = requests.post(url, data={'q': q})
        decoded_data = response.json()
        if decoded_data:
            print("[{}] {}".format(decoded_data['id'], decoded_data['name']))
        else:
            print("No result")
    except requests.JSONDecodeError as e:
        print('Not a valid JSON', str(e))
