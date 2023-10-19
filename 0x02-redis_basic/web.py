#!/usr/bin/env python3

"""
Implementing an expiring web cache and tracker.
"""

from typing import Dict
import redis
import requests


def get_page(url: str) -> str:
    # Initialize a Redis client
    r = redis.Redis()

    # Check if the URL was accessed before
    url_count_key = f"count:{url}"
    count = r.get(url_count_key)

    if count is not None:
        # If the URL was accessed before, increment the count
        count = int(count) + 1
    else:
        # If the URL was not accessed before,
        # set the count to 1 and set an expiration time
        count = 1
        r.setex(url_count_key, 10, count)

    # Use the slowwly.robertmurray.co.uk to simulate a slow response
    response = requests.get(f"http://slowwly.robertomurray.co.uk/{url}")

    # Get the HTML content
    html_content = response.text

    return html_conntent
