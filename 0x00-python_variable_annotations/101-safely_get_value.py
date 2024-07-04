#!/usr/bin/env python3
"""
This module provides a function to safely retrieve a value from a dictionary.
"""

from typing import Mapping, Any, Union, TypeVar

# Define a type variable ~T
T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary.

    Args:
        dct (Mapping): The dictionary-like object.
        key (Any): The key to lookup in the dictionary.
        default (Union[T, None], optional): The default value if key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value associated with key in dct, or default if key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default

