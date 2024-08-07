import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

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
    # ThreadPoolExecutor 생성
    with ThreadPoolExecutor() as executor:
        
        # 동기 함수 호출
        future1 = executor.submit(sync_simple_job)
        future2 = executor.submit(sync_simple_job)
        
        # sync_heavy_job의 결과를 기다림
        result1 = future1.result()
        result2 = future2.result()
        
        # sync_heavy_job2를 별도의 스레드에서 실행하도록 제출
        future3 = executor.submit(sync_heavy_job2)
        
        # 비동기 함수들을 asyncio.gather로 동시에 실행
        result3, result4 = await asyncio.gather(async_heavy_job1(), async_heavy_job2())

        # sync_heavy_job2의 결과를 기다림
        result5 = future3.result()

    # 모든 결과 합산
    total = result1 + result2 + result3 + result4 + result5
    print(f"Total: {total}")

if __name__ == "__main__":
    asyncio.run(main())
