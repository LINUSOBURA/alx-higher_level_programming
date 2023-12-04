#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        l = 1
        for x in i:
            if x == len(i):
                print ("{:d}".format(x), end="")
            else:
                print ("{:d}".format(x), end=" ")
            l += 1
        print()
