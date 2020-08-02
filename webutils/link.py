import url as uri

class QueryParams:
    
    def __init__(self):
        self.table = {}
        self.n = 0

    def add(**kwargs):
        tableKeys = set(self.table.keys())
        for s in tableKeys.union(set(kwargs.keys())):
            if self.table.get(s) == None:
                self.table[s] = [None] * n
            self.table[s].append(kwargs.get(s))
        self.n = self.n + 1

    def __str__(self):
        out = ""
        for k, v in self.table:
            out = out + f"{k}: {v}\n"
        return out

class Link:

    def __init__(self, url, data=None):
        if uri.isURL(url):
            self.url = url
        else:
            raise ValueError("Given url is not a URL")
        if isinstance(data, type({})):
            self.data = QueryParams()
            self.data.add(data)
        else:
            self.data = None
        
    def addData(data):
        if isinstance(data, type({})):
            if not isinstance(self.data, QueryParams):
                self.data = QueryParams()
            self.data.add(data)
            return True
        else:
            return False