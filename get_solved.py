import aiohttp
import asyncio

base_url = "https://leetcode.com/{}/"

def tasks(session, out):
    with open("users.txt", "r") as users:
        for user in users.readlines():
            yield GetSolved(session, user.strip(), out)

async def GetSolved(session, user, output):
    async with session.get(base_url.format(user), timeout=None) as res:
        page = await res.text()
        search = "badge progress-bar-success"
        spot = page.find("Progress")
        spot = page.find(search, spot)
        spot = page.find("\n", spot)
        end = page.find("\n", spot + 1)
        qns_solved = page[spot:end].strip()
        print("{} - {}".format(user, qns_solved))
        output.write("{},{}\n".format(user, ",".join(map(lambda x: x.strip(), qns_solved.split("/")))))

async def main(loop):
    async with aiohttp.ClientSession(loop=loop, headers={"Connection": "keep-alive"}) as session:
        with open("qns_solved.txt", "w") as out:
            await asyncio.gather(*tasks(session, out))

if __name__ == "__main__":
    # for i in users():
    #     print(i)
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main(event_loop))


