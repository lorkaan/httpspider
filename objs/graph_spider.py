from structs.graph import DirectedKeyGraph

from structs.bst import AvlTree
from structs.general import MaxHeap


class GraphSpiderError(Exception):
    pass

""" 
Alternative method to using a Spider that creates a Graph at
the same time as analyzing the Web Pages
"""
class GraphSpider:
    """ 
    Runs a Spider over the websites specified by a root url for
    a given depth.
    """


    def __init__(self, parseCls, urlCls):
        # Configurable Classes for Parsing and Handling URLs
        self.parseCls = parseCls
        self.urlCls = urlCls

        # Data Structures for Handling the processing
        self.parsedSet = AvlTree()
        self.nextCollection = MaxHeap()

        # Data Structure for Handling the results of processing each web page
        self.parseCollection = {}

        # Data Structures for Handling the Graph
        self.graph = DirectedKeyGraph()


    def webify(self, url, depth=0):
        if isinstance(depth, str):
            urlObj = self.urlCls.create(url)
            if urlObj != None:
                wPage = self.parseCls.parsePage(url)
                if not wPage in self.parsedSet:
                    self.parsedSet.insert(wPage)
                    if urlObj.getDomain() == depth:
                        self.parseCollection[wPage.getUrl()] = wPage.getParsedInfo()
                        self.graph.addVertex(wPage.getUrl())
                        for link in wPage.linkSet():
                            completeLink = urlObj.navigate(link)
                            self.graph.addVertex(completeLink)
                            self.graph.addEdge((url, completeLink)) # This does not understand query strings
                            if not completeLink in self.parsedSet:
                                self.nextCollection.add(completeLink, depth)
            else:
                print(f"Can not create URL Object from {url}")
            while self.nextCollection.peek() != None:
                nextUrl = self.nextCollection.next()
                self.webify(nextUrl[1], nextUrl[0])
            return self.parseCollection, self.graph
        elif isinstance(depth, int) and depth >= 0: # This is where the stopping point is checked.
            urlObj = self.urlCls.create(url)
            if urlObj != None:
                wPage = self.parseCls.parsePage(url)
                if not wPage in self.parsedSet:
                    self.parsedSet.insert(wPage)
                    self.parseCollection[wPage.getUrl()] = wPage.getParsedInfo()
                    self.graph.addVertex(wPage.getUrl())
                    for link in wPage.linkSet():
                        completeLink = urlObj.navigate(link)
                        self.graph.addVertex(completeLink)
                        self.graph.addEdge((url, completeLink)) # This does not understand query strings
                        if not completeLink in self.parsedSet:
                            self.nextCollection.add(completeLink, depth-1)
            else:
                print(f"Can not create URL Object from {url}")
            while self.nextCollection.peek() != None:
                nextUrl = self.nextCollection.next()
                self.webify(nextUrl[1], nextUrl[0])
            return self.parseCollection, self.graph
        else:
            # TO DO: Depth limited not by number but by host name
            return self.parseCollection, self.graph
    
    @staticmethod
    def run_spider(parseCls, urlCls, rootUrl, depth=0):
        try:
            anacii = GraphSpider(parseCls, urlCls)
        except TypeError as err:
            raise GraphSpiderError(f"Can not create GraphSpider Object because: {err}")
            anacii = None
        if isinstance(anacii, GraphSpider):
            return anacii.webify(rootUrl, depth)
        else:
            return {}, None