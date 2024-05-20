#!/usr/bin/python3
"""
This module contains a recursive function to query the Reddit API, parse
the title of all hot articles, and print a sorted count of given keywords.
"""
from collections import defaultdict
import requests


def count_words(subreddit, word_list, word_count=None, after=None):
    """
    Recursively queries the Reddit API, parses the titles of all hot
    articles, and prints a sorted count of given keywords (case-insensitive).

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): List of keywords to count in the titles.

    Returns:
        None
    """
    if word_count is None:
        word_count = defaultdict(int)

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
                'User-Agent':
                'python:subreddit.keyword.counter:v1.0 (by /u/yourusername)'}
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            after = data['data']['after']

            # Normalize word_list to lowercase
            normalized_word_list = [word.lower() for word in word_list]

            # Process titles and count keywords
            for post in posts:
                title = post['data']['title'].lower().split()
                for word in title:
                    clean_word = ''.join(filter(str.isalnum, word))
                    if clean_word in normalized_word_list:
                        word_count[clean_word] += 1

            if after:
                return (count_words(subreddit, word_list, word_count, after))
            else:
                # Sort and print the results
                sorted_word_count = sorted(
                        word_count.items(),
                        key=lambda item: (-item[1], item[0]))
                for word, count in sorted_word_count:
                    if count > 0:
                        print(f"{word}: {count}")
        else:
            return
    except requests.RequestException:
        return
