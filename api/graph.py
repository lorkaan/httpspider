from structs.graph import DirectedKeyGraph
from objs.graph_spider import GraphSpider
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

# This is the entry method to the new Graph Spider to be used
def createGraphSpider(urls, depth):
    if not isinstance(depth, int):
        raise TypeError("Expected depth to be an integer, but got {0}".format(type(depth)))
    if isinstance(urls, list):
        if len(urls) > 0:
            graphs = []
            for url in urls:
                if depth < 0:
                    cur_url = WebURL(url)
                    depth = cur_url.getDomain()
                try:
                    graph = GraphSpider.run_spider(NlpPage, WebURL, url, depth)
                except Exception as e:
                    print(e)
                    graph = None
                finally:
                    graphs.append(graph)
            return graphs
        else:
            return GraphSpider.run_spider(NlpPage, WebURL, urls, depth)
    else:
        if depth < 0:
            cur_url = WebURL(urls)
            depth = cur_url.getDomain()
        return GraphSpider.run_spider(NlpPage, WebURL, urls, depth)
