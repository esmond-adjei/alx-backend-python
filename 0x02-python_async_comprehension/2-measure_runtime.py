#!/usr/bin/env python3
"""
run time for four parallel comprehensions
"""

import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    runs `async_comprehension` four times in parallel
    using asyncio.gather and returns a total runtime
    """

    return asyncio.gather(*(async_comprehension() for _ in range(4)))
