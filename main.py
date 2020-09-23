#!/bin/env python3

import objs

if __name__ == '__main__':
    root = ""

    spider = objs.Spider(objs.Webpage)
    webSet = spider.parse()

    for page in webSet:
        print(page)