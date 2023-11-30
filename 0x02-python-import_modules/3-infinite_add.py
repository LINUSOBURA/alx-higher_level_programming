#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    pass

number_of_args = len(argv)
sum_of_args = 0
for n in range(1, number_of_args):
    sum_of_args = sum_of_args + int(argv[n])

print("{}".format(sum_of_args))
