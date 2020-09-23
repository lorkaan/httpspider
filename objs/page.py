import requests
from bs4 import BeautifulSoup

class WebPage:

    @classmethod
    def parsePage(cls, url):
        wPage = cls(url)
        try:
            resp = requests.get(url)
            soup = BeautifulSoup(resp.text, 'lxml')
            for link in soup.find_all('a'):
                if link.href in wPage.links:
                    continue
                else:
                    wPage.links.add(link['href'])
        finally:
            return wPage


    def __init__(self, url):
        self.url = url
        self.links = set()

    def linkSet(self):
        return self.links

    def __eq__(self, other):
        if isinstance(other, str):
            return self.url == other
        elif isinstance(other, type(self)):
            return self.url == other.url
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, str):
            return self.url < other
        elif isinstance(other, type(self)):
            return self.url < other.url
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, str):
            return self.url > other
        elif isinstance(other, type(self)):
            return self.url > other.url
        else:
            return False

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        retStr = self.url + "\n"
        for l in self.links:
            retStr = retStr + "\t" + l + "\n"
        return retStr

    