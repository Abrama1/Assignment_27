import asyncio
import random


async def random_delay():
    delay = random.randint(1, 5)
    print(f"Task 2 - Random Delay for {delay} seconds - Start")
    for i in range(1, 11):
        await asyncio.sleep(delay)
        print(i)
    print("Task 2 - Random Delay - End")

asyncio.run(random_delay())
