import asyncio

async def my_task(i):
    print(f"my_task {i} started")
    await asyncio.sleep(4)
    print(f"my_task {i} done")

async def main():
    task1 = asyncio.create_task(my_task(1))
    await asyncio.sleep(3)
    task2 = asyncio.create_task(my_task(2))
    await task1
    await task2

asyncio.run(main())

