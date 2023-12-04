#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for x in range(len(i)):
            print("{:d}".format(i[x]), end=" " if x < len(i) - 1 else "")
        print()
