#!/bin/env python3
import sys
import objs
from structs.graph import DirectedKeyGraph

def createGraph(urls, depth):
    spider = objs.Spider(objs.NlpPage, objs.WebURL)
    dGraph = DirectedKeyGraph()
    for url in urls:
        webSets, parsedInfo = spider.parse(url, depth)
        webList = webSets.generateList()
        for webPage in webList:
            dGraph.addVertex(webPage.getUrl())
            for link in webPage.linkSet():
                dGraph.addVertex(link)
                dGraph.addEdge((webPage.getUrl(), link))
    return dGraph, parsedInfo
    

if __name__ == '__main__':
    '''
    root = sys.argv[1]
    spider = objs.Spider(objs.WebPage, objs.WebURL)
    
    webSet = spider.parse(root, int(sys.argv[2]))
    for page in webSet.generateList():
        print(page)
    '''
    root = sys.argv[1]
    graph, parsedInfo = createGraph([root], int(sys.argv[2]))
    print(graph)
    print("\t------ Parsed Info -----\n")
    counter = 0
    for key, val in parsedInfo.items():
        print(f"{counter}:  {key}\t{val}\n")
        counter = counter + 1