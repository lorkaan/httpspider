#!/bin/env python3

import objs

if __name__ == '__main__':
    root = "https://www.google.com/search?sxsrf=ALeKk00uZ0RbQzcAt1a5bOEtsjTPTVG03A%3A1600827191190&source=hp&ei=N69qX4vUCY3e5gKWgqfYDw&q=html&oq=html&gs_lcp=CgZwc3ktYWIQAzIECCMQJzIECCMQJzIFCAAQsQMyBQgAELEDMgUIABCxAzIFCAAQsQMyBQgAELEDMgUIABCxAzICCAAyBQgAELEDOggIABCxAxCDAToLCC4QsQMQxwEQowJQt0RY4Udg4ktoAHAAeACAAYcBiAHoA5IBAzAuNJgBAKABAaoBB2d3cy13aXo&sclient=psy-ab&ved=0ahUKEwjLy82Amv7rAhUNr1kKHRbBCfsQ4dUDCAc&uact=5"

    spider = objs.Spider(objs.WebPage)
    webSet = spider.parse(root, 1)

    for page in webSet.generateList():
        print(page)