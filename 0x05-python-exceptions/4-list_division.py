#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    if my_list_1 == None or my_list_2 == None:
        my_list_1 = []
        my_list_2 = []

    for i in range(list_length):
        try:
            value_1 = my_list_1[i] if i < len(my_list_1) else None
            value_2 = my_list_2[i] if i < len(my_list_2) else None

            if value_1 is None or value_2 is None:
                raise IndexError("out of range")

            result = value_1 / value_2
            new_list.append(result)
        except (FloatingPointError, TypeError):
            print("wrong type")
            new_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
            break
    return new_list
