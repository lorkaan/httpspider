from structs.graph import DirectedKeyGraph
from parsers.pages.nlpPage import NlpPage
import objs

def createGraph(urls, depth):
    spider = objs.Spider(NlpPage, objs.WebURL)
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