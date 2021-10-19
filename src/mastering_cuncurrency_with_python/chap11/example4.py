import aiohttp
import asyncio

async def get_html(session, url):
    async with session.get(url, ssl=False) as res:
        return await res.text()

async def main():
    # this whole context block itself will be treated as coroutine
    async with aiohttp.ClientSession() as session:
        html = await get_html(session, "https://packtpub.com")
        print(html)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
