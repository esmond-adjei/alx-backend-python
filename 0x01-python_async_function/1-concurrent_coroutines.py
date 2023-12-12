#!/usr/bin/env python3
"""
execute multiple coroutines at the same time with async
"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    Asynchronous routine that spawns wait_random n times
    with the specified max_delay.

    :param n: Number of times to spawn wait_random.
    :param max_delay: Maximum delay in seconds.
    :return: List of delays in ascending order.
    """

    # delays = [wait_random(max_delay) for _ in range(n)]
    # return await asyncio.gather(*delays)
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)
