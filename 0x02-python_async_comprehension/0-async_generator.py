#!/usr/bin/env python3
"""
async generator
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    loops 10 times during which it waits 1 seconnd and generates
    a random number between 0 and 10.
    """

    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
