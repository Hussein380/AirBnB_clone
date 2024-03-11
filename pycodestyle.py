#!/usr/bin/python3

def swap_numbers(a, b):
    """
    swap integer a and b
    :wq
    a: the first integer to be swappd
    b: the second integer to be swappedi

    """
    temp = a
    a = b
    b = temp
    return (a, b)


print(swap_numbers(2, 5))
