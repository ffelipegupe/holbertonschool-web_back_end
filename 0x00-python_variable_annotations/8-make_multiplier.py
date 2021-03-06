#!/usr/bin/env python3
""" Complex types - functions """

import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """  function make_multiplier that takes a float multiplier as argument
        and returns a function that multiplies a float by multiplier. """
    def func(float: float):
        """ Helper function """
        return float * multiplier
    return func
