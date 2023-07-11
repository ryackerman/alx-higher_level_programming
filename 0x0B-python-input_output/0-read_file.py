#!/usr/bin/python3
"""A function that reads a text file"""


def read_file(filename=""):
    """func prints content of a text file (UTF8) to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
