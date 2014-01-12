#!/usr/bin/python
from bs4 import BeautifulSoup
from urllib2 import urlopen
from Scraper import Scraper

# uses the superclass's scrape
class fsoeScraper(Scraper):
    
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