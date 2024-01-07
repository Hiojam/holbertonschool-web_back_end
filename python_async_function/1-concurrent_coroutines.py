#!/usr/bin/env python3
"""
Asynchronous coroutine
"""
from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Return a list of all the delays in ascending order.

    Args:
    - n (int): The number of delays to generate.
    - max_delay (int): The maximum delay value.

    Returns:
    - List[float]: A list of all the generated delays in ascending order.
    """
    completed_task_lst = []

    for _ in range(n):
        # Await and store the result of the asynchronous call
        completed_task_lst.append(await wait_random(max_delay))

    return sorted(completed_task_lst)
