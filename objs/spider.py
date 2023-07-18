from structs.bst import AvlTree
from structs.general import MaxHeap

class Spider:

    def __init__(self, clsObj, urlCls):
        self.parseCls = clsObj
        self.urlCls = urlCls

    def _handle_url_clash(self, cur_url, next_url):
        pass

    def webify(self, url, depth=0, parsedSet=None, nextCollection=None, parseCollection=None):    
        if not isinstance(parsedSet, AvlTree):
            parsedSet = AvlTree()
        if not isinstance(parseCollection, dict):
            parseCollection = {}
        if not isinstance(nextCollection, MaxHeap):
            nextCollection = MaxHeap()
        if depth >= 0:
            urlObj = self.urlCls.create(url)
            if urlObj != None:
                wPage = self.parseCls.parsePage(url)
                if not wPage in parsedSet:
                    parsedSet.insert(wPage)
                    parseCollection[wPage.getUrl()] = wPage.getParsedInfo()
                for link in wPage.linkSet():
                    completeLink = urlObj.navigate(link)
                    if completeLink in parsedSet:
                        _handle_url_clash(url, completeLink)
                    else:
                        nextCollection.add(completeLink, depth-1)
            else:
                print(f"Can not create URL Object from {url}")
            while nextCollection.peek() != None:
                nextUrl = nextCollection.next()
                self.webify(nextUrl[1], nextUrl[0], parsedSet, nextCollection, parseCollection)
            return parsedSet, parseCollection
        else:
            return parsedSet, parseCollection
        

    def parse(self, rootUrl, depth=0):
        return self.webify(rootUrl, depth)
    