#!/usr/bin/python3
"""
This module contains a recursive function to query the Reddit API and
return a list of titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively queries the Reddit API and returns a list containing the
    titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit, returns None.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list, optional): A list to store the titles of hot
        articles. Defaults to None.
        after (str, optional): A token indicating the starting point
        for the next page of results. Defaults to None.

    Returns:
        list: A list of titles of hot articles, or None if the
        subreddit is invalid.
    """
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 100}  # Retrieve up to 100 posts per request

    if after:
        params["after"] = after

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()["data"]
        posts = data["children"]
        for post in posts:
            hot_list.append(post["data"]["title"])

        # Check if there are more pages of results
        after = data.get("after")
        if after:
            return (recurse(subreddit, hot_list, after))
        else:
            return (hot_list if hot_list else None)
    else:
        return (None)
