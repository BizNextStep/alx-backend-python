#!/usr/bin/env python3
"""
This module contains a function that returns an asyncio.Task.
"""

import asyncio
from 0-basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio.Task for the wait_random coroutine.

    Args:
        max_delay (int): Maximum delay for wait_random.

    Returns:
        asyncio.Task: An asyncio.Task object.
    """
    return asyncio.create_task(wait_random(max_delay))

