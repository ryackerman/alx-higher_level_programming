#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_integers = set()

    for item in my_list:
        if isinstance(item, int):
            unique_integers.add(item)

    total = sum(unique_integers)

    return total
