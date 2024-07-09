#!/usr/bin/env python3
"""Module for async comprehension"""

from typing import List
from 0_async_generator import async_generator

async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using an async comprehensing
    over async_generator, then returns the 10 random numbers.
    """
    return [number async for number in async_generator()]

