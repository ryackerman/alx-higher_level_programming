#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request,
displays the body of the response"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    val = {"email": sys.argv[2]}
    body = urllib.parse.urlencode(val).encode("ascii")

    rq = urllib.request.Request(url, body)
    with urllib.request.urlopen(rq) as res:
        print(res.read().decode("utf-8"))
