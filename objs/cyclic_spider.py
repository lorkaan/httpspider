from spider import Spider


"""
This is a Spider that Creates a Cyclic Directed Graph
"""
class CyclicSpider(Spider):

    def __init__(self, clsObj, urlCls):
        super().__init__(clsObj, urlCls)
        self.edges = []

    def _handle_url_clash(self, url):
        pass