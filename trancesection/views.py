from trancesection import app
from flask import render_template
from scrapers import Scraper, AbgtScraper
from trancesection.models import Podcast,Episode,Track

@app.route('/')
@app.route('/index')
def index():

	import pdb; pdb.set_trace()
	episode_list = Episode.query.order_by(Episode.created_on).limit(10).all()
	episodes = [(Podcast.query.get(x.podcast_id).name, x) for x in episode_list]
	podcasts = Podcast.query.limit(3).all()
	return render_template('index.html',podcasts=podcasts, episodes=episodes)


@app.route('/<podcast>')
def podcast(podcast):
 	return render_template('podcast.html')

# @app.route('/<podcast>/<episode>')
# def episode():
# 	return render_template('episode.html')

#@app.route('/<podcast>/<episode>/<track>')
#def track():
# 	return render_template('track.html')
