#!/usr/bin/python3

def swap_numbers(a, b):
    """swap integer a and b"""
    temp = a
    a = b
    b = temp
    return (a, b)

print(swap_numbers(2,5))
