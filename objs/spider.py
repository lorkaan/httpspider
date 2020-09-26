from structs.bst import AvlTree

class Spider:

    def __init__(self, clsObj, urlCls):
        self.parseCls = clsObj
        self.urlCls = urlCls

    def webify(self, url, depth=0, parsedSet=None, nextCollection=None):    
        if not isinstance(parsedSet, AvlTree):
            parsedSet = AvlTree()
        if not isinstance(nextCollection, list):
            nextCollection = []
        if depth > 0:
            urlObj = self.urlCls.create(url)
            if urlObj != None:
                wPage = self.parseCls.parsePage(url)
                if not wPage in parsedSet:
                    parsedSet.insert(wPage)
                for link in wPage.linkSet():
                    completeLink = urlObj.navigate(link)
                    if completeLink in parsedSet:
                        continue
                    else:
                        nextCollection.append(completeLink)
            else:
                print(f"Can not create URL Object from {url}")
            if len(nextCollection) > 0:
                nextUrl = nextCollection.pop(0)
                return self.webify(nextUrl, depth-1, parsedSet, nextCollection)
            else:
                return parsedSet
        else:
            return parsedSet
        

    def parse(self, rootUrl, depth=0):
        return self.webify(rootUrl, depth)
    