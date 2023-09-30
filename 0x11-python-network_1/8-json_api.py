#!/usr/bin/python3
"""8. Search API"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) < 2:
        letter = ""
    else:
        letter = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    data = {"q": letter}


    req = requests.post(url, data=data)
    try:
        res = req.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a valid JSON")
