# Pulls problems solved by users from leetcode by scraping the website

should be easy to generalize in order to scrape websites that have per-user data but not overall stats

To run, make you have Python 3+ and Selenium + driver for Chrome

`pip install asyncio aiohttp selenium itertools time`

then

`python get_users.py` then `python get_solved.py`

* slower but should be more random

or

`python get_contest_users.py` then `python get_contest_solved.py` or `python get_contest_ratings.py`

* faster but should be less random
