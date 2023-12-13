#!/usr/bin/env python3
"""
async generator
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    loops 10 times during which it waits 1 seconnd and generates
    a random number between 0 and 10.
    :return: async generator of random float numbers
    """

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
