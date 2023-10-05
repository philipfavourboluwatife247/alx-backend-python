#!/usr/bin/env python3

"""
 Write a type-annotated function to_kv
 that takes a string k and an int OR
 float v as arguments and returns a
 tuple. The first element of the
 tuple is the string k.
 The second element is the square of
 the int/float v and should be
 annotated as a float.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with the string k
    as the first element and the
    square of int/float v as the
    second element
    """
    squared_v: float = float(v ** 2)
    return k, squared_v
