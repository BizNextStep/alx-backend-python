#!/usr/bin/env python3
"""Module to measure runtime of parallel async comprehensions"""

import asyncio
import time
from typing import List
from 1_async_comprehension import async_comprehension

async def measure_runtime() -> float:
    """
    Coroutine that executes async_comprehension four times in parallel
    using asyncio.gather. Measures and returns the total runtime.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    total_time = time.time() - start_time
    return total_time

