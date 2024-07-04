#!/usr/bin/env python3
"""
This module provides a function to return a tuple with a string and the square of an int/float.
"""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with the string and the square of the int/float.

    Args:
        k (str): The string.
        v (Union[int, float]): The integer or float number.

    Returns:
        Tuple[str, float]: The string and the square of the number.
    """
    return (k, float(v ** 2))

