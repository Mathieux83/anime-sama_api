from anime_sama_api import AnimeSama, find_site_url
from httpx import AsyncClient
import asyncio


semaphore = asyncio.Semaphore(10)

async def scan(catalogue):
    async with semaphore:
        return await catalogue.state()

async def async_main() -> None:

    client = AsyncClient()
    url = await find_site_url(client, "https://anime-sama.pw/")

    if url is None:
        raise

    catalogues = await AnimeSama(url, client).search("")
    await asyncio.gather(*(scan(catalogue) for catalogue in catalogues))

asyncio.run(async_main())
