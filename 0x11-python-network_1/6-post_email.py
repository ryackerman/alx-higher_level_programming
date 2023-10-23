#!/usr/bin/python3
"""6. POST an email #1"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    val = {"email": sys.argv[2]}

    req = requests.post(url, val)
    print(req.text)
