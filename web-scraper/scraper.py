import requests
import time
from random import randint
import re
from bs4 import BeautifulSoup
from rich import print
from rich.console import Console


def get_page(_url):
    response = requests.get(_url)
    time.sleep(2)
    if response.status_code == 200:
        return BeautifulSoup(response.content, "html.parser")

def get_citations_needed_count(_page):
    citations = _page.find_all("a", {"title": "Wikipedia:Citation needed"})

    return print(len(citations))

def get_citations_needed_report(_page):
    citations = _page.find_all("a", {"title": "Wikipedia:Citation needed"})
    for citation in citations:
        filter_one = citation.parent.parent.parent.text.strip('[citation needed]\n')
        filter_two = re.sub("[\(\[].*?[\)\]]", "", filter_one)
        Console().log(filter_two, style="bold blue on black", justify="left")


if __name__ == '__main__':
    url = "https://en.wikipedia.org/wiki/Israeli%E2%80%93Palestinian_conflict"
    page = get_page(url)
    get_citations_needed_count(page)
    get_citations_needed_report(page)



