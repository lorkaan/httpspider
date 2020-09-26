import webutils as wutil

class Query:

    def __init__(self, query):
        self._storage = {}
        args = query.split("&")
        for arg in args:
            params = arg.split("=", 1)
            self._storage[params[0]] = params[1]

    def get(self, key):
        return self._storage.get(key, None)

class WebURL:

    @classmethod
    def create(cls, url):
        try:
            return cls(url)
        except:
            return None

    def __init__(self, url):
        pIndex, lIndex = wutil.getProtocol(url)
        if pIndex == lIndex:
            raise Exception("Can not get Protocol URL")
        elif wutil.isHttpResource(url[pIndex:lIndex]):
            self._protocol = url[pIndex:lIndex]
        else:
            raise Exception("Protocol is not a Web Resource")
        dStart, dEnd = wutil.getDomain(url, lIndex)
        if dStart == dEnd:
            raise Exception("Domain could not be found")
        else:
            self._domain = url[dStart:dEnd]
        _, query = wutil.separateQuery(url)
        if query == None or len(query) <= 0:
            # create the query object
             self._query = None
        else:
            # No Query
            self._query = Query(query)

    def getProtocol(self):
        return self._protocol

    def getDomain(self):
        return self._domain

    def getQuery(self):
        return self._query

    def navigate(self, newUrl):
        pIndex, lIndex = wutil.getProtocol(newUrl)
        if pIndex == lIndex:
            protocol = self.getProtocol()
        else:
            protocol = newUrl[pIndex:lIndex]
        dStart, dEnd = wutil.getDomain(newUrl, lIndex)
        if dStart == dEnd:
            domain = self.getDomain()
        else:
            domain = newUrl[dStart:dEnd]
        return protocol + domain + newUrl[dEnd:]