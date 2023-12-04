#!/usr/bin/python3

if __name__ == "__main__":
    pass


def element_at(my_list, idx):
    len_of_list = len(my_list)
    if idx < 0 or idx > len_of_list - 1:
        return (None)
    else:
        return(my_list[idx])
