#!/usr/bin/env python3

"""import wait_random from 0-basic_async_syntax
and write a function (do not create an async function,
use the regular function syntax to do this) task_wait_random
that takes an integer max_delay and returns a asyncio.Task"""

wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio
from typing import List

def task_wait_random(max_delay: int) -> asyncio.Task:
    """task wait random takes max delay and returns a asyncio.Task"""
    return asyncio.create_task(wait_random(max_delay))