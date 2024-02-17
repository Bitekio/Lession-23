""" Homework """

import time
import requests
import asyncio
import aiohttp


async def fetch_url(url):
    """Выполняет асинхронный HTTP запрос по указанному URL и возвращает текст ответа."""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def fetch_from_multiple_urls(urls):
    """Выполняет асинхронный HTTP запрос к нескольким URL и возвращает текст ответа для каждого URL."""
    tasks = [fetch_url(url) for url in urls]
    return await asyncio.gather(*tasks)


def run_without_async():
    """Выполняет неасинхронные HTTP GET-запросы к нескольким URL и замеряет время выполнения."""
    start_time = time.time()
    urls = ["https://jsonplaceholder.typicode.com/posts"] * 100
    for url in urls:
        requests.get(url)
    end_time = time.time()
    print("Время выполнения без асинхронности:", end_time - start_time)


async def run_with_async():
    """Выполняет асинхронные HTTP GET-запросы к нескольким URL и замеряет время выполнения."""
    start_time = time.time()
    urls = ["https://jsonplaceholder.typicode.com/posts"] * 100
    await fetch_from_multiple_urls(urls)
    end_time = time.time()
    print("Время выполнения с асинхронностью:", end_time - start_time)


async def main():
    """запуск кода"""
    await run_with_async()


if __name__ == "__main__":
    asyncio.run(main())
