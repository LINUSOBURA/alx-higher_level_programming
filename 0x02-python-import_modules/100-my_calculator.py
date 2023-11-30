#!/usr/bin/python3

from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    pass

number_of_args = len(argv)

if number_of_args < 4 or number_of_args > 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)

a = int(argv[1])
b = int(argv[3])
operator = argv[2]

if operator == "+":
    result = add(a, b)
elif operator == "-":
    result = sub(a, b)
elif operator == "*":
    result = mul(a, b)
elif operator == "/":
    result = div(a, b)
else:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)

print("{} {} {} = {}".format(a, b, operator, result))
