#!/usr/bin/env python3
from typing import Callable

"""
Write a type-annotated function make_multiplier that takes a float multiplier
as argument and returns a function that multiplies a float by multiplier
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    returns a function that multiplies a float by the multiplier.
    """
    def multiplier_func(x: float) -> float:
        return x * multiplier
    return multiplier_func
