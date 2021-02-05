#!/usr/bin/python3
""" To know top 10 hot titles for a subreddit"""
import requests


def top_ten(subreddit):
    """Return first 10 hotest title from subreddit"""
    try:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        url = requests.get(url, headers={'User-agent': 'me'},
                           allow_redirects=False).json()

        a = url.get("data")
        b = a.get("children")
        ind = 0

        while ind < 10:
            print(b[ind].get("data").get("title"))
            ind += 1
    except:
        print(None)
