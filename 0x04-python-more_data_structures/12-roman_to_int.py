#!/usr/bin/python3


def roman_to_int(roman_string):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50,
             "C": 100, "D": 500, "M": 1000}
    if type(roman_string) != str or roman_string is None:
        return 0

    total_value = 0
    prev_value = 0
    for char in reversed(roman_string):
        if char in roman:
            current_value = roman[char]
            if current_value >= prev_value:
                total_value += current_value
            else:
                total_value -= current_value
            prev_value = current_value

    return total_value
