from spider import Spider


# Pretty sure the Graph Spider already creates cyclic graphs, just refuses to parse
# the completed links a second time

"""
This is a Spider that Creates a Cyclic Directed Graph
"""
class CyclicSpider(Spider):

    def __init__(self, clsObj, urlCls):
        super().__init__(clsObj, urlCls)
        

    def _handle_url_clash(self, url):
        pass