#!/usr/bin/env python3
"""
This module provides a function to sum a list of integers and float numbers.
"""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums a list of integers and float numbers.

    Args:
        mxd_lst (List[Union[int, float]]): The list of integers and float numbers.

    Returns:
        float: The sum of the numbers.
    """
    return sum(mxd_lst)

