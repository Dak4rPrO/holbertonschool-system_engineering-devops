#!/usr/bin/python
""" function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) """

import json
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """ return the number of subscribers
    (not active users, total subscribers)"""
    try:
        user_agent = {'User-agent': 'Mozilla/5.0'}
        subreddit = requests.get('https://www.reddit.com/r/{}/about.json'
                                 .format(subreddit), headers=user_agent)
        return (subreddit.json()['data']['subscribers'])
    except Exception:
        return 0
