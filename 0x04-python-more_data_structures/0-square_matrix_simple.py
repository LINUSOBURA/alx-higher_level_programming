#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new_matrix = [row[:] for row in matrix]
    for i in range(len(new_matrix)):
        new_list = []
        for value in new_matrix[i]:
            square = value * value
            new_list.append(square)
        new_matrix[i] = new_list
    return new_matrix
