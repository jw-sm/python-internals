import asyncio


async def hello_world() -> str:
    await asyncio.sleep(3)
    return "Hello World!"


async def main() -> None:
    message = await hello_world()
    print("testingggg")
    print(message)
    print("wadadeng")


asyncio.run(main())
