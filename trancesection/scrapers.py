#!/usr/bin/python
from bs4 import BeautifulSoup
from urllib2 import urlopen
from trancesection import app
import xml.etree.ElementTree as et
from multiprocessing.dummy import Pool as ThreadPool

from copy_reg import pickle
from types import MethodType

from trancesection import db
from trancesection.models import Podcast, Episode, Track


#Need this because instance methods are not pickleable..
def scraper_process_wrapper(scraper,episode):
    scraper.scrape_episode(episode)

class Scraper(object):

    def __init__(self):
        pass

    def add_episode_to_db(self,podcast,episode_name,track_list):

        #Create new podcast
        podcast_id = Podcast.query.filter_by(name=podcast).first().id
        episode = Episode(episode_name,podcast_id)
        db.session.merge(episode)

        #Flush so we can know the episode id
        db.session.flush()
 
        #add tracks
        for track in track_list:
            track = Track(track,episode.id)
            db.session.add(track)

        db.session.commit()
        db.session.close()

    def scrape(self):
        raise NotImplementedError

class FsoeScraper(Scraper):

     def __init__(self):
        self.index_url = app.config['FSOE_RSS_URL']

     def scrape_episode(self, url):
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

     def scrape(self):
        pass

class AbgtScraper(Scraper):
    def __init__(self):
        self.index_url = app.config['ABGT_RSS_URL']
        self.podcast_name = 'Group Therapy'

    def get_episode_urls(self):
        """ Get every episode url so we can scrape them """
        try:
            page = urlopen(self.index_url)
        except:
            return []

        xml_string = page.read()
        root = et.fromstring(xml_string)
        #find all urls from the rss feed (with a little hack to get only the ABGT podcasts)
        urls = [ep.find('link').text for ep in root[0].findall('item') if '.mp3' not in ep.find('link').text]
        #another hack because the first episodes links are broken for some reason...
        urls[0] = 'http://www.aboveandbeyond.nu/radio/abgt001'
        urls[1] = 'http://www.aboveandbeyond.nu/radio/abgt002'
        urls[2] = 'http://www.aboveandbeyond.nu/radio/abgt003'
        urls[3] = 'http://www.aboveandbeyond.nu/radio/abgt004'
        urls[4] = 'http://www.aboveandbeyond.nu/radio/abgt005'

        return urls

    def scrape_episode(self, url):
        """Scrapes the episode and adds it to the DB"""
        print('parsing episode %s' % url)
        try:
            page = urlopen(url)
        except:
            print 'got a 404..:('
            return

        ep_name = url.rsplit('/',1)[1]
        soup = BeautifulSoup(page)
        raw = soup.get_text()
        block = raw.split('\n\n')
        tracks = ''
        for i in block:
            if (len(i) > 2):
                if (i[1] == '.' or i[2] == '.'):
                    tracks = i
        rawList = tracks.split('\n')
        track_list = [i[i.find('.')+2:len(i)] for i in rawList if i.find('.') != -1]

        #Found the track list now add it to db
        self.add_episode_to_db(self.podcast_name,ep_name,track_list)

    def scrape(self):
        """ Scrape and add to database """
        episodes = self.get_episode_urls()
        pool = ThreadPool(4)
        episodes = pool.map(lambda x:scraper_process_wrapper(self,x), episodes)
        pool.close()
        pool.join()
        return episodes

class IntDeptScraper(Scraper):
    def __init__(self):
        self.index_url = app.config['ID_RSS_URL']

    def get_track_list_from_rss(self, rss_text):
        block = rss_text.split('\n\n')
        tracks = ''
        for i in block:
            if (len(i) > 0):
                if (i[2] == '.'):
                    tracks = i
        rawList = tracks.split('\n')
        trackList = [i[4:len(i)] for i in rawList if (i[2] == '.') ]
        return trackList

    # returns a dict of ep:tracklist
    def scrape(self, url):
        page = urlopen('url')
        xml_string = page.read()
        root = et.fromstring(xml_string)
        track_dict = {}
        for ep in root[0].findall('item'):
            if ep.find('description').text[2] == '.':
                ep_name = ep.find('title').text
                tracklist = [track[track.find('.')+2:] for track in ep.find('description').text.split('\n')]
                add_episode_to_db(ep_name, tracklist)
                
class AsotScraper(Scraper):

    def __init__(self):
        super(AsotScraper, self).__init__('http://www.astateoftrance.com/podcasts/podcast-')

    def getTracks(self, url):
        try:
            page = urlopen(url)
        except:
            return []
        soup = BeautifulSoup(page)
        raw = soup.findAll('ol')
        soup = BeautifulSoup(str(raw[0]))
        artists = [i.text for i in soup.findAll('strong')]
        rawList = raw[0].text.strip().split('\n')
        trackList = [j.replace(i, i + ' - ', 1) for i, j in zip(artists, rawList)]
        return trackList
