#!/usr/bin/env python3
"""
This module provides a function to zoom in an array by repeating elements.
"""

from typing import Tuple, List

def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> Tuple[int, ...]:
    """
    Zooms in an array by repeating elements.

    Args:
        lst (Tuple[int, ...]): The input tuple of integers.
        factor (int, optional): The factor by which to zoom in. Defaults to 2.

    Returns:
        Tuple[int, ...]: The zoomed-in tuple of integers.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return tuple(zoomed_in)


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)  # Corrected to use an integer instead of a float
