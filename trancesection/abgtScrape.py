#!/usr/bin/python
from bs4 import BeautifulSoup
from urllib2 import urlopen


#returns empty list if cannot open page
def getTracks(url):
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

def urlNum(num):
    if type(num) == int:
        num = str(num)
    if len(num) < 3:
        while (len(num) < 3):
            num = '0' + num

    url = 'http://www.aboveandbeyond.nu/radio/abgt%s' % num
    return getTracks(url)
