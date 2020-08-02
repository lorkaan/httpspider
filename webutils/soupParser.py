from bs4 import BeautifulSoup
import sendHttp

def getSoup(url, **kwargs):
    try:
        resp = send('get', url, **kwargs)
    except:
        raise
    else:
        return BeautifulSoup(resp.text, 'lxml')
'''
Extracts the a tags from a given BeauitfulSoup
'''
def extractHrefs(url, **kwargs):
    soup = getSoup(ur, **kwargs)l)
    a_list = soup.find_all('a')
    hrefList = []
    for elem in a_list:
        try:
            hrefList.append(elem['href'])
        except:
            continue
    return hrefList

'''
Extract Text from the BeautifulSoup
'''
def extractText(url, **kwargs)):
    return getSoup(url, **kwargs)).get_text()