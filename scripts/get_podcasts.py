#!/usr/bin/env python

from multiprocessing.dummy import Pool as ThreadPool
from trancesection.scrapers import AbgtScraper

# Add other scrapers here ~
SCRAPERS = [AbgtScraper()]

def main():
	# Making a pool of 4 workers (Should play with that number to see whats best)
	pool = ThreadPool(4)
	# Call scrape on each scraper


if __name__ == "__main__":
	main()