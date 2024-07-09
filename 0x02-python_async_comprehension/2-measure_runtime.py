#!/usr/bin/env python3
'''Asynchronous Python
'''
import asyncio
from typing import List
from __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    '''Measure the total runtime of executing async_comprehension four times in parallel
    '''
    start_time = asyncio.current_time()
    await asyncio.gather(async_comprehension(), async_comprehension(), async_comprehension(), async_comprehension())
    end_time = asyncio.current_time()
    return end_time - start_time
