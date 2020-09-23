import requests
from bs4 import BeautifulSoup

class WebPage:

    @classmethod
    def parsePage(cls, url):
        wPage = cls()
        try:
            resp = requests.get(url)
            soup = BeautifulSoup(resp.text, 'lxml')
            for link in soup.find_all('a'):
                if link.href in wPage.links:
                    continue
                else:
                    wPage.links.add(link.href)
        finally:
            return wPage


    def __init__(self):
        self.links = set()

    