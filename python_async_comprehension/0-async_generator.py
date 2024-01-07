#!/usr/bin/env python3
"""
Asynchronous coroutine that generates random floats
"""
import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """
    Asynchronous generator that yields random float values.

    Yields:
    - float: Random float values within the range of 0 to 10.
    """
    for _ in range(0, 10):
        # Asynchronously wait for 1 second
        await asyncio.sleep(1)
        # Yield a random float value between 0 and 10
        yield random.uniform(0, 10)
