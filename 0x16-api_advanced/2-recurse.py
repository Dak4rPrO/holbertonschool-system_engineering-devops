#!/usr/bin/python3
"""function that queries the Reddit API and prints the titles of the first 10
    hot posts listed for a given subreddit."""


import requests


def top_ten(subreddit):
    user_agent = {'User-agent': 'Mozilla/5.0'}
    count = 0
    try:
        r = requests.get('https://www.reddit.com/r/{}/hot.json'
                         .format(subreddit), headers=user_agent, allow_redirects=False)
        r2 = r.json()['data']['children']
        for title in r2:
            if (count < 10):
                print(title['data']['title'])
            count += 1
    except Exception:
        print(None)
