import urllib2
import BeautifulSoup
import itertools
import re

def getLinks():
	#website were going to
	craig = "https://binghamton.craigslist.org/search/cta?hasPic=1&searchNearby=1"

	page = urllib2.urlopen(craig)

	from bs4 import BeautifulSoup

	soup = BeautifulSoup(page, 'html.parser')
	
	#get each individual post
	links = soup.select('li.result-row')

	#get just the link for each post
	for e in links:
		e = e.a['href']

	return links

file = open('output.txt','w')










#file.write(str(soup))

file.close()