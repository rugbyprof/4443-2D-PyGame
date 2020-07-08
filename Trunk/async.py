#!/usr/bin/python3

import time
import asyncio

def is_prime(x):
    return not any(x // i == x / i for i in range(x - 1, 1, -1))

async def highest_prime_below(x):
    print(f"Highest below {x}: ")
    for y in range(x - 1, 0, -1):
        if is_prime(y):
            print(f"-> Highest prime below {x} is {y}.")
            return y
        await asyncio.sleep(0.1)
        #time.sleep(0.01)
    return None

async def main():
    await highest_prime_below(100000)
    await highest_prime_below(10000)
    await highest_prime_below(1000)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()