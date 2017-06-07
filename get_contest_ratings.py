import aiohttp
import asyncio

base_url = "https://leetcode.com/{}/"

def tasks(session, out):
    with open("users_contest.txt", "r") as users:
        for user in users.readlines():
            yield GetRating(session, user.strip(), out)

async def GetRating(session, user, output):
    async with session.get(base_url.format(user), timeout=None) as res:
        page = await res.text()
        search = "badge progress-bar-success"
        spot = page.find("Contest")
        spot = page.find(search, spot)
        spot = page.find(search, spot + 1)
        spot = page.find("\n", spot)
        spot = page.find("\n", spot + 1)
        end = page.find("\n", spot + 1)
        rating = page[spot:end].strip()
        print("{} - {}".format(user, rating))
        output.write("{},{}\n".format(user, rating))

async def main(loop):
    async with aiohttp.ClientSession(loop=loop, headers={"Connection": "keep-alive"}) as session:
        with open("ratings_contest.txt", "w") as out:
            await asyncio.gather(*tasks(session, out))

if __name__ == "__main__":
    # for i in users():
    #     print(i)
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main(event_loop))

