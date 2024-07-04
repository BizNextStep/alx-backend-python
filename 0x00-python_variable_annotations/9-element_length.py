#!/usr/bin/env python3
"""
This module provides a function to return tuples of elements and their lengths.
"""

from typing import Iterable, Sequence, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns tuples of elements and their lengths.

    Args:
        lst (Iterable[Sequence]): The iterable of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples containing elements and their lengths.
    """
    return [(i, len(i)) for i in lst]
