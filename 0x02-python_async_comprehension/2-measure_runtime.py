#!/usr/bin/env python3
""" Run time for four parallel comprehensions """
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Will execute async_comprehension four times in parallel using
        asyncio.gather. measure_runtime should measure the total runtime
        and return it. """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    return end_time - start_time
