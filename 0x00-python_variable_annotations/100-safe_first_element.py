#!/usr/bin/env python3
"""
This module provides a function to safely retrieve the first element of a sequence.
"""

from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence) -> Union[Any, None]:
    """
    Safely retrieves the first element of a sequence.

    Args:
        lst (Sequence): The input sequence.

    Returns:
        Union[Any, None]: The first element of the sequence, or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None

