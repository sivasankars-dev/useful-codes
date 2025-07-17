import asyncio

async def task(name):
    print(f'{name} is started')
    await asyncio.sleep(2)
    print(f'{name} is finished')

async def main():
    await asyncio.gather(
        task('task1'),
        task('task2')
    )

asyncio.run(main())