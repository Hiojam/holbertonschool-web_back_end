#!/usr/bin/env python3
"""
Measure execution time for asynchronous coroutine wait_n
"""
import asyncio
import time


wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure execution time for the wait_n coroutine
    and return the average time taken per coroutine call.

    Args:
    - n (int): The number of coroutines to run.
    - max_delay (int): The maximum delay value for each coroutine.

    Returns:
    - float: The average time taken per coroutine call.
    """
    start = time.time()
    # Run the wait_n coroutine 'n' times concurrently
    asyncio.run(wait_n(n, max_delay))
    end = time.time()

    total_time = end - start
    # Calculate the average time per coroutine call
    return total_time / n
