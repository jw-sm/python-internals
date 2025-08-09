import asyncio
from util import delay


async def main():
    delay_task = asyncio.create_task(delay(7))

    try:
        result = await asyncio.wait_for(asyncio.shield(delay_task), 5)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print("Task took longer than 5 seconds, it will finish soon!")
        result = await delay_task
        print(result)


asyncio.run(main())
