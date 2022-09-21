#!/usr/bin/python3
"""function that queries the Reddit API and prints the titles of the first 10
    hot posts listed for a given subreddit."""


import requests


def top_ten(subreddit):
    user_agent = {'User-agent': 'Mozilla/5.0'}
    try:
        r = requests.get('https://www.reddit.com/r/{}/hot.json'
                         .format(subreddit), headers=user_agent)
        return r.json()['data']['subscribers']
    except Exception:
        return 0
