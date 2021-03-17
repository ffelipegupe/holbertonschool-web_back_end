#!/usr/bin/env python3
""" Measuring the runtime"""

import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """ function with integers n and max_delay as arguments that measures the
        total execution time for wait_n(n, max_delay), and returns
        total_time / n """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start
    return total_time / n
