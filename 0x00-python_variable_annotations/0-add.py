#!/usr/bin/env python3
""" Basic annotations - add """


def add(a: float, b: float) -> float:
    """ Fucntion that returns the sum of two floats """
    return a + b



print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)