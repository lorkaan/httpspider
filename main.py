#!/bin/env python3

import objs

if __name__ == '__main__':
    root = ""

    spider = objs.Spider(objs.WebPage)
    webSet = spider.parse(root, 1)

    for page in webSet:
        print(page)