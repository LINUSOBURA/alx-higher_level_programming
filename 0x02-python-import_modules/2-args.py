#!/usr/bin/python3
if __name__ == "__main__":
    pass

import sys

argv = sys.argv

number_of_args = len(argv)

if number_of_args == 1:
        print("0 arguments.")
else:
    if number_of_args == 2:
        print("{} argument:".format(number_of_args-1))
    else:
        print("{} arguments:".format(number_of_args-1))
    for n in range (1, number_of_args):
        print("{}: {}".format(n, argv[n]))
