#!/usr/bin/python3
""" To know number of subs"""
import requests


def number_of_subscribers(subreddit):
    """Return number of subs from subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    url = requests.get(url, headers={'User-agent': 'your bot 0.1'}).json()

    if "subscribers" in url["data"]:
        return url["data"].get("subscribers")
    else:
        return 0
