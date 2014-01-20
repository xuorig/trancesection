from trancesection import app
from flask import render_template
from scrapers import Scraper, AbgtScraper
from trancesection.models import Podcast,Episode,Track
from trancesection import init_db
import soundcloud

sc_client = soundcloud.Client(client_id='e926a44d2e037d8e80e98008741fdf91')

@app.route('/')
@app.route('/index')
def index():
	episode_list = Episode.query.order_by(Episode.created_on).limit(10).all()
	episodes = [(Podcast.query.get(x.podcast_id).name, x) for x in episode_list]
	podcasts = Podcast.query.limit(6).all()
	return render_template('index.html',podcasts=podcasts, episodes=episodes)


@app.route('/podcasts')
def podcasts():
	podcasts = Podcast.query.all()
 	return render_template('podcasts.html',podcasts=podcasts)

@app.route('/podcasts/<podcast>')
def podcast(podcast):
 	pc = Podcast.query.filter_by(slug=podcast).first()
 	episodes = pc.episodes
 	return render_template('podcast.html',pc=pc,episodes=episodes)

@app.route('/podcasts/<podcast>/<episode>')
def episode(podcast,episode):
 	epi = Episode.query.filter_by(number=episode).first()
 	pc = Podcast.query.filter_by(slug=podcast).first()
 	pcname = pc.name
 	tracks = epi.trax.all()
 	print tracks
 	return render_template('episode.html',episode=epi,pcname=pcname,tracks=tracks)

@app.route('/tracks/<trackname>/')
def track(trackname):
 	tr = Track.query.filter_by(slug=trackname).first()
 	embed_info = sc_client.get('/oembed', url=tr.soundcloud_url)
 	trackhtml = embed_info.html
	return render_template('track.html',tr=tr,trackhtml=trackhtml)

