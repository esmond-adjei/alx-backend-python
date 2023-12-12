#!/usr/bin/env python3
"""
Tasks
"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns task_wait_random
    n times with the specified max_delay.

    :param n: Number of times to spawn task_wait_random.
    :param max_delay: Maximum delay in seconds.
    :return: List of delays.
    """
    delays = await asyncio.gather(
        *(task_wait_random(max_delay) for _ in range(n)))
    return sorted(delays)
