### Original code adapted from https://realpython.com/lru-cache-python/
### Modified for additional functionality

import feedparser
import requests
import ssl
import time


from functools import lru_cache, wraps
from datetime import datetime, timedelta

if (hasattr(ssl, "_create_unverified_context")):
        ssl._create_default_https_context = ssl._create_unverified_context


def timed_lru_cache(seconds: int, maxsize: int = 128):
    def wrapper_cache(func):
        func = lru_cache(maxsize = maxsize)(func)
        func.lifetime = timedelta(seconds = seconds)
        func.expiration = datetime.utcnow() + func.lifetime


        @wraps(func)
        def wrapped_func(*args, **kwargs):
            if datetime.utcnow() >= func.expiration:
                func.cache_clear()
                func.expiration = datetime.utcnow() + func.lifetime

            return func(*args, **kwargs)

        return wrapped_func

    return wrapper_cache


@timed_lru_cache(10)
def get_article_from_server(url):
    response = requests.get(url)
    return response.text


def monitor(url):
    # title length
    maxlen = 200
    # this would normally loop indefinitely.  
    # Edit: exiting after retreiving all feeds and logging them.
    while True:
        print("\nChecking feed...")
        feed = feedparser.parse(url)

        # Set the max feed entries to retrieve
        for entry in feed.entries[:50]:
#            if "python" in entry.title.lower():
            if searchKeyword in entry.title.lower():
                truncated_title = (
                        entry.title[:maxlen] + "..."
                        if len(entry.title) > maxlen
                        else entry.title
                        )
                print(
                        "Match found:",
                        truncated_title,
                        len(get_article_from_server(entry.link)),
                        )
                try:
                    fp = open("./" + logDir + "/" + listFileName[siteIndex]
                            + logExt, "a")
                    fp.write(truncated_title + ";" + entry.link + "\n")

                finally:
                    fp.close
            
                time.sleep(3)
        return



# Update to remove hardcoded search keywords
# Example rss & atom URLs (could probably be added to a dictionary)
listURLs = [ "Https://news.google.com/news/rss/search?q={inflation}", 
        "Https://news.google.com/news/rss/search?q={yen}", 
        "https://www.reddit.com/r/girlsfrontline/.rss",
        "https://www.reddit.com/r/cyberpunkgame/.rss",
        "https://realpython.com/atom.xml"]

# Log file containing URL and Titles
listFileName = [ "news.google", "news.google", "girlsfrontline",
        "cyberpunk2077", "realpython"]

# log file extension
logExt = ".dat"

# log directory
logDir = "dat"

# search keyword in title (Example: python, tesla, etc.) 
# or can use space
searchKeyword = " "

# - index of the lists above to retrieve.  
# - if needed, could probably add a loop for the entire list on
# on a daily basis.
siteIndex = 2

# zero out any existing logs
open("./" + logDir + "/" + listFileName[siteIndex] + logExt, "w").close()
monitor(listURLs[siteIndex])

            



