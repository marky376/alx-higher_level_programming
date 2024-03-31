#!/usr/bin/python3
"""10 most recent commits on a given GitHub repository.
"""
import sys
import requests

if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(
        owner_name, repository_name)

    response = requests.get(url, auth=(owner_name, repository_name))
    commit_list = response.json()

    try:
        for i in range(10):
            print("{}: {}".format(
                commit_list[i]["sha"],
                commit_list[i]["commit"]["author"]["name"]))
    except IndexError:
        pass
