from structs.bst import AvlTree

class Spider:

    def __init__(self, clsObj):
        self.parseCls = clsObj

    def webify(self, url, depth=0, parsedSet=None, nextCollection=None):
        if not isinstance(parsedSet, AvlTree):
            parsedSet = AvlTree()
        if not isinstance(nextCollection, list):
            nextCollection = []
        if depth > 0:
            wPage = self.parseCls.parsePage(url)
            if not wPage in parsedSet:
                parsedSet.insert(wPage)
            for link in wPage.linkSet():
                if link in parsedSet:
                    continue
                else:
                    nextCollection.append(link)
            if len(nextCollection) > 0:
                nextUrl = nextCollection.pop(0)
                return self.webify(nextUrl, depth-1, parsedSet, nextCollection)
            else:
                return parsedSet
        else:
            return parsedSet
        

    def parse(self, rootUrl, depth=0):
        return self.webify(rootUrl, depth)
    