#!/usr/bin/env python3

"""
Given the parameters and the
return values, add type annotations to the function.
Hint: look into TypeVar
"""


from typing import Mapping, Any, Union, TypeVar

# Create a type variable for the return type
T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Safely get a value from a dictionary.

    :param dct: A mapping (e.g., dictionary-like object).
    :param key: The key to look up in the mapping.
    :param default: An optional value of type T or None.
    :return: A value that can be either of type Any or T.
    """
    if key in dct:
        return dct[key]
    else:
        return default
