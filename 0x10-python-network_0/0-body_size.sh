#!/bin/bash
# This script sends a GET request to a URL and displays the body of the response
curl -sI "$1" | grep 'Content-Length' | cut -d' ' -f2`
