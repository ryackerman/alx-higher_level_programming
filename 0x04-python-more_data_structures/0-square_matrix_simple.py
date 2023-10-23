#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    res = []
    for i in matrix:
        j = []
        for n in i:
            j.append(n * n)

        res.append(j)
    return res
