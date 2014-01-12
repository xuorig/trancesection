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

# uses the superclass's scrape
class FsoeScraper(Scraper):

    def __init__(self):
        super(fsoeScraper, self).__init__('http://www.futuresoundofegypt.com/radio/fsoe')

    def getTracks(self, url):
        try:
            page = urlopen(url)
        except:
            return []
        soup = BeautifulSoup(page)
        raw = soup.findAll('ol')
        tracks = raw[0].text
        tracks = tracks.strip()
        trackList = tracks.split('\n')
        return trackList

class AbgtScraper(Scraper):
    def __init__(self):
        super(abgtScraper, self).__init__('http://www.aboveandbeyond.nu/radio/abgt')

    #returns empty list if cannot open page
    def getTracks(self, url):
        try:
            page = urlopen(url)
        except:
            return []
        soup = BeautifulSoup(page)
        raw = soup.get_text()
        block = raw.split('\n\n')
        tracks = ''
        for i in block:
            if (len(i) > 0):
                if (i[0] == '1'):
                    tracks = i
        rawList = tracks.split('\n')
        trackList = [i[i.find('.')+1:len(i)] for i in rawList]
        return trackList

    def scrape(self, num):
        if type(num) == int:
            num = str(num)
        if len(num) < 3:
            while (len(num) < 3):
                num = '0' + num

        url = 'http://www.aboveandbeyond.nu/radio/abgt%s' % num
        return self.getTracks(url)


