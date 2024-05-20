#!/usr/bin/python3
"""
This module contains a recursive function to query the Reddit API and
return a list of titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the
    titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit, returns None.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): The list of titles collected so far.
        after (str): The "after" parameter for pagination.

    Returns:
        list: A list of titles of hot articles, or None if the
        subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'
               User-Agent':
               'python:subreddit.hot.posts:v1.0 (by /u/yourusername)'}
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            children = data['data']['children']
            after = data['data']['after']

            if not children:
                return (hot_list if hot_list else None)

            for child in children:
                hot_list.append(child['data']['title'])

            if after:
                return (recurse(subreddit, hot_list, after))
            else:
                return (hot_list)
        else:
            return (None)
    except requests.RequestException:
        return (None)
