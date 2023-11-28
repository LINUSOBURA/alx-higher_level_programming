#!/usr/bin/python3
def islower(c):
    for char in range(97, 123):
        lower = chr(char)
        if c == lower:
            return True
    return False
