from trancesection import app
from flask import render_template
from scrapers import Scraper, AbgtScraper
from trancesection.models import Podcast,Episode,Track
from trancesection import init_db

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

# @app.route('/podcasts/<podcast>/<episode>')
# def episode(podcast,episode):
# 	return render_template('episode.html')

#@app.route('/podcasts/<podcast>/<episode>/<track>')
#def track():
# 	return render_template('track.html')