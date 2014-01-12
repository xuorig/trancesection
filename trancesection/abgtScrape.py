#!/usr/bin/python
from bs4 import BeautifulSoup
from urllib2 import urlopen



def getTracks(url):
    page = urlopen(url)
    soup = BeautifulSoup(page)
    raw = soup.get_text()
    block = raw.split('\n\n')
    tracks = ''
    for i in block:
        if (len(i) > 0):
            if (i[0] == '1'):
                tracks = i

    rawList = tracks.split('\n')
    trackList = []
    for i in rawList:
        index = i.find('.')
        trackList.append(i[index+1:len(i)])

    return trackList

getTracks("http://www.aboveandbeyond.nu/radio/abgt058")