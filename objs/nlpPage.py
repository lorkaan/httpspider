import requests
from bs4 import BeautifulSoup
from .page import WebPage
from parsers.nlp import nlpUtils as nlp

class NlpPage(WebPage):

    @classmethod
    def parsePage(cls, url, significantThreshold=10):
        wPage = cls(url)
        try:
            resp = requests.get(url)
            soup = BeautifulSoup(resp.text, 'lxml')
            for link in soup.find_all('a'):
                if link.href in wPage.links:
                    continue
                else:
                    wPage.links.add(link['href'])
            wPage.topicWords = nlp.getSignificant(soup.get_text(), significantThreshold)
        finally:
            return wPage

    def __init__(self, url):
        super().__init__(url)
        self.topicWords = {}

    def getParsedInfo(self):
        return self.topicWords

    def getFreq(self, word):
        if isinstance(word, str):
            return self.topicWords.get(word.lower(), 0)
        else:
            return 0
    
    def getWordList(self):
        words = []
        for key, _ in self.topicWords.items():
            words.append(key)
        return words

    def __str__(self):
        cur = super().__str__()
        for key, val in self.topicWords.items():
            cur += f"\t\t{key}: {val}\n"
        return cur