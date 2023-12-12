#!/usr/bin/env python3
"""
Tasks
"""
import asyncio
from typing import Coroutine


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task for wait_random with the
    specified max_delay.

    :param max_delay: Maximum delay in seconds.
    :return: asyncio.Task for wait_random.
    """
    coro = wait_random(max_delay)
    task = asyncio.create_task(coro)
    return task
