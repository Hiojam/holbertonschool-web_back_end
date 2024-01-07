#!/usr/bin/env python3
"""Asynchronous coroutine for creating multiple tasks"""
from typing import List


task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Return a list of all the delays in ascending order.

    Args:
    - n (int): The number of tasks to create.
    - max_delay (int): The maximum delay value for each task.

    Returns:
    - List[float]: A list of all the generated delays in ascending order.
    """
    completed_task_lst = []

    for _ in range(n):
        # Wait for and store the result of the task
        completed_task_lst.append(await task_wait_random(max_delay))

    return sorted(completed_task_lst)
