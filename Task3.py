import asyncio


async def calculate_square(number):
    print(f"Task 3 - Calculating Square for {number}")
    await asyncio.sleep(1)
    return number ** 2


async def is_even(number):
    print(f"Task 3 - Checking if {number} is Even")
    await asyncio.sleep(1)
    return number % 2 == 0


async def task3():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    tasks = [calculate_square(num) for num in numbers]
    squares = await asyncio.gather(*tasks)
    print("Squares:", squares)

    tasks_even = [is_even(num) for num in squares]
    results = await asyncio.gather(*tasks_even)
    for num, is_even_num in zip(squares, results):
        print(f"{num} is {'even' if is_even_num else 'odd'}")

asyncio.run(task3())
