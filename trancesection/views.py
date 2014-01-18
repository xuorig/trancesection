from trancesection import app
from flask import render_template
from scrapers import Scraper, AbgtScraper

@app.route('/')
@app.route('/index')
def index():
    #testing the scrapers...
    import pdb; pdb.set_trace()
    return render_template('index.html')


@app.rout('/<podcast>')
def podcast():
	pass

@app.route('/<podcast>/<episode>')
def episode():
	pass

@app.route('/<podcast>/<episode>/<track>')
def track():
	pass
