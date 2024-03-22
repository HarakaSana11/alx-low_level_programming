#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    empty = []
    for x in matrix:
        empty.append(list(map(lambda x: x**2, x)))
    return (empty)
