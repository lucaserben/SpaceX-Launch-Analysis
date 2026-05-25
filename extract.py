import requests
from logs import log

def fetch(url):
    log(f"Fetching URL: {url}")
    return requests.get(url, timeout=15)

