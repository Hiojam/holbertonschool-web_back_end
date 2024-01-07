#!/usr/bin/env python3
"""
Asynchronous coroutine that generates a random delay
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Generate a random delay and return it.

    Args:
    - max_delay (int): The maximum value for the delay (default 10).

    Returns:
    - float: A randomly generated delay between 0 and max_delay.
    """
    # Generate a random delay within the specified range
    delay = random.uniform(0, max_delay)

    # Pause the coroutine for the calculated delay
    await asyncio.sleep(delay)

    return delay
