#!/usr/bin/env python3
"""
This module provides a function to create a multiplier function.
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The multiplier to create the function.

    Returns:
        Callable[[float], float]: A function that takes a float and returns its multiplication by multiplier.
    """
    def multiplier_function(num: float) -> float:
        return num * multiplier
    
    return multiplier_function

