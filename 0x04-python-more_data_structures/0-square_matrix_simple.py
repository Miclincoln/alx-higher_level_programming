#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return ([list(map(lambda n: n ** 2, mat_list)) for mat_list in matrix])
