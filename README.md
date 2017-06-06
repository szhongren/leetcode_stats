# Pulls problems solved by users from leetcode

Done with the basic brute-force method of generating all possible usernames and pulling data from the given page, but cannot scale

Better method, pulls usernames from the contest rankings with Selenium

To run, make you have Python 3+

`pip install asyncio aiohttp selenium itertools time`

then

`python get_users.py` then `python get_solved.py`

* slower but should be more random

or

`python get_contest_users.py` then `python get_contest_solved.py`

* faster but should be less random
