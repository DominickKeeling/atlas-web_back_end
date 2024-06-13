#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into a new function task_wait_n. The
code is nearly identical to wait_n except task_wait_random is being called.
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random
from typing import List


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Returns list of delays
    """
    opperations = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*opperations)
    return sorted(results)
