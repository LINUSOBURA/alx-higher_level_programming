#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    if my_list is None:
        my_list = []
    int_printed = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            int_printed += 1
        except (ValueError, TypeError):
            pass
    print()
    return int_printed

