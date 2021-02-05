#!/usr/bin/python3
""" To know number of subs"""
import requests


def number_of_subscribers(subreddit):
    """Return number of subs from subreddit"""
    try:
        url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
        url = requests.get(url, headers={'User-agent': 'your bot 0.1'},
                       allow_redirects=False).json()
        return url["data"].get("subscribers")
    except:
        return 0
