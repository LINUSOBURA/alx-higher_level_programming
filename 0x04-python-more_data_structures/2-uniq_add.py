#!/usr/bin/python3


def uniq_add(my_list=[]):
    my_set = set(my_list)
    my_result = 0
    for i in my_set:
        my_result += i
    return my_result
