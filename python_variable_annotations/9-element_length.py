#!/usr/bin/env python3

"""
Annotate the below function’s parameters and return values with the appropriate
types

def element_length(lst):
    return [(i, len(i)) for i in lst]
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    returns an iterable from thee list
    """
    return [(i, len(i)) for i in lst]
