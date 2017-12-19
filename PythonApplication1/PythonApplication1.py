import urllib2
import BeautifulSoup
import itertools
import re
from bs4 import BeautifulSoup

def getLinks():
	#website were going to
	craig = "https://binghamton.craigslist.org/search/cta?hasPic=1&searchNearby=1"

	page = urllib2.urlopen(craig)

	soup = BeautifulSoup(page, 'html.parser')
	
	#get each individual post
	links = soup.select('li.result-row')

	newList = []

	#get just the link for each post
	for e in links:
		newList.append(e.a['href'])

	return newList

def iterate(u):
	page = urllib2.urlopen(u)
	soup = BeautifulSoup(page, 'html.parser')
	list = soup.select('p.attrgroup')
	print list
	

file = open('output.txt','w')

theLinks = getLinks()

iterate(theLinks[0])

#for e in theLinks:
	#iterate(e)







#file.write(str(soup))

file.close()