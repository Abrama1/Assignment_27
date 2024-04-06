import asyncio


async def delay_2_seconds():
    print("Task 1 - Delay 2 seconds - Start")
    await asyncio.sleep(2)
    print("Task 1 - Delay 2 seconds - End")


async def delay_5_seconds():
    print("Task 1 - Delay 5 seconds - Start")
    await asyncio.sleep(5)
    print("Task 1 - Delay 5 seconds - End")


async def task1():
    task1_1 = asyncio.create_task(delay_2_seconds())
    task1_2 = asyncio.create_task(delay_5_seconds())
    await task1_1
    await task1_2

asyncio.run(task1())
