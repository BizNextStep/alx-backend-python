#!/usr/bin/env python3
'''Asynchronous Python
'''
from typing import List
from __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    '''Create a list of 10 random numbers from the imported generator
    '''
    return [num async for num in async_generator()]
