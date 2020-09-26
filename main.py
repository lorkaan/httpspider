#!/bin/env python3
import sys

import objs

if __name__ == '__main__':
    root = sys.argv[1]

    spider = objs.Spider(objs.WebPage)
    webSet = spider.parse(root, int(sys.argv[2]))

    for page in webSet.generateList():
        print(page)