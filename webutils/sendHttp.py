import requests

# http methods
http = {
    'get': requests.get,
    'post': requests.post,
    'head': requests.head,
    'put': requests.put,
    'delete': requests.delete,
    'options': requests.options
}

def send(method, url, **kwargs):
    try:
        reqFunc = http[method]
    except:
        raise
    else:
        return reqFunc(url, **kwargs)


    