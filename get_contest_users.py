import aiohttp
import asyncio
import time
from selenium import webdriver

base_url = "https://leetcode.com/contest/globalranking/{}/"

def pages():
    for page in range(1, 367):
        yield page

def HandlePage(driver, page, output):
    driver.get(base_url.format(page))
    time.sleep(1)
    names = driver.find_elements_by_class_name("ranking-username")
    for i, name in enumerate(names):
        link = name.get_attribute("href")
        user = link.split('/')[-1]
        print("{} - {}: {}".format((page - 1) * 50 + i, link, user))
        output.write("{}\n".format(user))

def main():
    # async with aiohttp.ClientSession(loop=loop, headers={"Connection": "keep-alive"}) as session:
    driver = webdriver.Chrome()
    with open("users_contest.txt", "w") as out:
        for page in pages():
            HandlePage(driver, page, out)
    driver.close()

if __name__ == "__main__":
    main()
