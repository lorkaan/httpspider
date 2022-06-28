from structs.graph import DirectedKeyGraph
from parsers.pages.nlpPage import NlpPage
from web.weburl import WebURL
from objs.spider import Spider

def createGraph(urls, depth):
    spider = Spider(NlpPage, WebURL)
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