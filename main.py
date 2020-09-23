#!/bin/env python3

from objs import WebPage, Spider

if __name__ == '__main__':
    root = ""

    spider = Spider(Webpage)
    webSet = spider.parse()

    for page in webSet:
        print(page)