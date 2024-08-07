import asyncio
import time

async def async_heavy_job1():
    await asyncio.sleep(3)
    print(3)
    return 3

async def async_heavy_job2():
    await asyncio.sleep(4)
    print(4)
    return 4

def sync_simple_job():
    print(1)
    return 1

def sync_heavy_job2():
    time.sleep(5)
    print(5)
    return 5

async def main():
    # Sync function calls
    result1 = sync_simple_job()
    result2 = sync_simple_job()
    result5 = sync_heavy_job2()

    # Async function calls with asyncio.gather to run concurrently
    result3, result4 = await asyncio.gather(async_heavy_job1(), async_heavy_job2())

    # Adding all results
    total = result1 + result2 + result3 + result4 + result5
    print(f"Total: {total}")

if __name__ == "__main__":
    asyncio.run(main())
