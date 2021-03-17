#!/usr/bin/env python3
""" Executeing multiple coroutines at the same time with async """

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """  async routine called wait_n that takes in 2 int arguments
        (in this order): n and max_delay. You will spawn wait_random n times
        with the specified max_delay. """
    delays: List[float] = []
    for _ in range(n):
        delays.append(wait_random(max_delay))
    return [await delay for delay in asyncio.as_completed(delays)]
