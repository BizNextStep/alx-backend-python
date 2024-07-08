#!/usr/bin/env python3
'''Asynchronous Python
'''
from typing import List
import asyncio


time_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Return a list of awaited responses from the previous function
    '''
    res = await asyncio.gather(
        *tuple(map(lambda _: time_wait_random(max_delay), range(n)))
    )
    return sorted(res)
