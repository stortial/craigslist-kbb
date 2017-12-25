import urllib2
import BeautifulSoup
import itertools
import re
from bs4 import BeautifulSoup
#import rhinoscriptsyntax as rs
import json

def getLinks():
	#website were going to
	craig = "https://binghamton.craigslist.org/search/cta?hasPic=1&searchNearby=1"

	#opens the webpage and stores it in soup
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
	#gets the webpage nad stores it as soup
	soup = BeautifulSoup(page, 'html.parser')

	#gets the list of things on the side and saves it under list
	list = soup.find_all("p", "attrgroup")
	
	#get the title ex "2008 gmc 1500 sierra" and expunge it of the whitespace
	title = list[0].text
	title = title.strip()

	parse(title)
	
def parse(t):
	#find the year
	year = re.match(r'\d\d\d\d',t)
	#make = any(x in MAKES for c in t)#with makes being the list of all car makes
	#model = re.match()
	#print year.group()

file = open('output.txt','w')

#opens the list of all car makes and models
with open('car-list.json', 'r') as f:
	data = json.load(f)

for k,v in data.iteritems():
	print(k,v)

#theLinks = getLinks()

#iterate(theLinks[0])

#for e in theLinks:
	#iterate(e)

	 





#file.write(str(soup))

file.close()