import aiohttp
import asyncio
import itertools

base_url = "https://leetcode.com/{}/"
num_letters = 4

def users():
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    for count in range(1, num_letters):
        for name in itertools.product(chars, repeat=count):
            yield "".join(name)

def tasks(session, out):
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    for count in range(1, num_letters):
        for name in itertools.product(chars, repeat=count):
            yield CheckHeader(session, "".join(name), out)

async def CheckHeader(session, user, output):
    async with session.head(base_url.format(user), timeout=None) as res:
        print("{} - {}".format(res.status, user))
        if res.status != 200:
            return await res.release()
        output.write("{}\n".format(user))
        return await res.release()

async def main(loop):
    async with aiohttp.ClientSession(loop=loop, headers={"Connection": "keep-alive"}) as session:
        with open("actual_users.txt", "w") as out:
            await asyncio.gather(*tasks(session, out))

if __name__ == "__main__":
    # for i in users():
    #     print(i)
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main(event_loop))

