#!/usr/bin/python3
def uppercase(string):
    for char in string:
        ascii_chr = ord(char)
        if ascii_chr >= 97 and ascii_chr <= 122:
            char = chr(ascii_chr - 32)
        print("{:s}".format(char), end='')
    print('\n', end="")
