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
        if len(query) <= 0:
            # create the query object
             self._query = Query(query)
        else:
            # No Query
            self._query = None

    def getProtocol(self):
        return self._protocol

    def getDomain(self):
        return self._domain

    def getQuery(self):
        return self._query