#!/usr/bin/env python3
"""
basics of async
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay
    between 0 and max_delay

    :param max_delay: Maximum delay in seconds (default = 10).
    :return: Random delay.
    """

    delay = random.uniform(0, max_delay + 1)
    await asyncio.sleep(max_delay)
    return delay
