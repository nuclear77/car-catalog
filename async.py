import aiohttp
import asyncio
import threading
import time

from base import data

async def search_x():
    global data
    start_time = time.time()
    result = [char for char in data if char == 'x']
    end_time = time.time()
    print(f"Threading {threading.current_thread().name} found {len(result)} occurrences of 'x' in {end_time - start_time:.4f} seconds.")


async def main():
    tasks = [search_x() for _ in range(4)]  # 4 потока для параллельного поиска
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())