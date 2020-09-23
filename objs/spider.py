
class Spider:

    def __init__(self, clsObj):
        self.parseCls = clsObj

    def webify(self, url, parsedSet=None, nextCollection=None):
        wPage = self.parseCls.parsePage(url)
        if not isinstance(parsedSet, set):
            parsedSet = set()
        if not isinstance(nextCollection, list):
            nextCollection = []
        if not wPage in parsedSet:
            parsedSet.add(wPage)
        for link in wPage.linkSet():
            if link in parsedSet():
                continue
            else:
                nextCollection.append(link)
        if len(nextCollection) > 0:
            nextUrl = nextCollection.pop(0)
            return self.webify(nextUrl, parsedSet, nextCollection)
        else:
            return parsedSet
        

    def parse(self, rootUrl):
        return self.webify(rootUrl)
    