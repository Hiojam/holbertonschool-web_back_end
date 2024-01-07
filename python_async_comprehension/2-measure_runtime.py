#!/usr/bin/env python3
"""Measure total runtime of async_comprehension"""

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Execute async_comprehension four times in parallel using asyncio.gather.

    Returns:
    - float: The total runtime of executing
         async_comprehension four times in parallel.
    """
    start_time = asyncio.get_event_loop().time()

    # Run async_comprehension() four times in parallel using asyncio.gather
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = asyncio.get_event_loop().time()

    return end_time - start_time
