#!/usr/bin/env python3

"""
 Annotate the below function’s
 parameters and return values with
 the appropriate types

 def element_length(lst):
    return [(i, len(i)) for i in lst]
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each
    element in the input iterable of
    sequences and return a list of tuples.
    Each tuple contains an element
    and its length.
    """
    return [(i, len(i)) for i in lst]
