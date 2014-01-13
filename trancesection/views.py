from trancesection import app
from flask import render_template
from scrapers import Scraper, AbgtScraper

@app.route('/')
@app.route('/index')
def index():
    #testing the scrapers...
    abgt = AbgtScraper()
    print('tast')
    res = abgt.scrape()
    return render_template('index.html')
