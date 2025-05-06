#!/usr/bin/python3

import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if len(sys.argv) != 2:
    print("Usage: ./factorial.py <non-negative integer>")
    sys.exit(1)

try:
    number = int(sys.argv[1])
    if number < 0:
        f = factorial(number)
        print(f)
except ValueError as e:
    print("Error:", e)
    sys.exit(1)
