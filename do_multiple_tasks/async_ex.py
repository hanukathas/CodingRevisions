import asyncio

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    await say_after(1, 'hello')
    await say_after(2, 'world')

if __name__ == '__main__':
    print("Starting async tasks...")
    asyncio.run(main())
    print("Async tasks completed.")