"""
https://docs.python.org/3/library/asyncio-task.html#coroutine
"""

import asyncio
import time

async def firstname():
    print("Task firstname: Computing")
    await asyncio.sleep(4)
    return 'Bolaji'


async def lastname():
    print("Task lastname: Computing")
    await asyncio.sleep(3)
    return 'blog.bolaji.de'


async def nick():
    print("Task nick: Computing")
    await asyncio.sleep(5)
    # raise ValueError
    return 'Proton'


async def main():
    print(f"started at {time.strftime('%X')}")
    result = await asyncio.gather( # loses it's cool if any of the awaitables return an error
        firstname(),
        lastname(),
        nick()
    )
    print(f"finished at {time.strftime('%X')}")
    print('\n\n\n\n')
    print(result)


asyncio.run(main())

"""
Expected result
---------------

started at 23:30:34
Task firstname: Computing
Task lastname: Computing
Task nick: Computing
finished at 23:30:39





['Bolaji', 'blog.bolaji.de', 'Proton']
"""
