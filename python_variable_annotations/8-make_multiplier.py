#!/usr/bin/env python3

"""
Write a type-annotated function make_multiplier that takes a float multiplier
as argument and returns a function that multiplies a float by multiplier.
"""
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiplier_function(x: float) -> float:
        """
        Takes a float, multiplies it to the multiplier and returns the product"""
        return x * multiplier

    """
    Returns the multiplier function to the main.
    """
    return multiplier_function