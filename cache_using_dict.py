import requests

cache = dict()

def get_article_from_server(url):
    print("fetching article from server...")
    response = requests.get(url)
    return response.text


def get_article(url):
    print("Getting article...")
    if url not in cache:
        cache[url] = get_article_from_server(url)
    else:
        print("retrieving article from cache")

    return cache[url]

get_article("https://realpython.com/sorting-algorithms-python/")
get_article("https://realpython.com/sorting-algorithms-python/")
