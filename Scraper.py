#!/usr/bin/python
from bs4 import BeautifulSoup
from urllib2 import urlopen

# scraper superclass

class Scraper(object):
    # base is url without episode number
    def __init__(self, base):
        self.base = base

    def getTracks(self, url):
        raise NotImplementedError

    def scrape(self, num):
        if type(num) == int:
            num = str(num)
        url = self.base + num
        return self.getTracks(url)
