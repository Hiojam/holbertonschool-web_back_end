#!/usr/bin/env python3
""" Asynchronous task creation """
import asyncio


wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asynchronous task for wait_random.

    Args:
    - max_delay (int): The maximum delay value for wait_random.

    Returns:
    - asyncio.Task: An asynchronous task for wait_random with the specified max_delay.
    """
    return asyncio.create_task(wait_random(max_delay))
