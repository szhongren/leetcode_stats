import aiohttp
import asyncio

base_url = "https://leetcode.com/contest/globalranking/{}/"

def tasks(session, out):
    for page in range(1, 367):
        yield HandlePage(session, page, out)

async def HandlePage(session, page, output):
    async with session.get(base_url.format(page), timeout=None) as res:
        page = await res.text()
        spot = page.find("tbody")
        print(page[spot: spot + 40])
        output.write(page)

async def main(loop):
    async with aiohttp.ClientSession(loop=loop, headers={"Connection": "keep-alive"}) as session:
        with open("contest_users.txt", "w") as out:
            await asyncio.gather(*tasks(session, out))

if __name__ == "__main__":
    # for i in users():
    #     print(i)
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main(event_loop))


