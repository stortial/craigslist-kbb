from __future__ import unicode_literals
import urllib.request
import itertools
import re
from bs4 import BeautifulSoup
#import rhinoscriptsyntax as rs
import json

#gets the links for each post
def getLinks():
	#website were going to
	craig = "https://binghamton.craigslist.org/search/cta?hasPic=1&searchNearby=1"

	#opens the webpage and stores it in soup
	page = urllib.request.urlopen(craig)
	soup = BeautifulSoup(page, 'html.parser')

	#get each individual post
	links = soup.select('li.result-row')

	newList = []

	#get just the link for each post
	for e in links:
		newList.append(e.a['href'])
	print (newList[0])

	return newList

#gets the title from the post and parses it
def iterate(u):
	page = urllib.request.urlopen(u)
	#gets the webpage nad stores it as soup
	soup = BeautifulSoup(page, 'html.parser')

	#gets the list of things on the side and saves it under list
	list = soup.find_all("p", "attrgroup")

	#get the title ex "2008 gmc 1500 sierra" and expunge it of the whitespace
	title = list[0].text
	title = title.strip()

	return parse(title)

#TODO - finish parse
#get make and model
#make year proper number ie dosent take in 1500 from "chevy siverado 1500"
#finish style
def parse(t):

	#find the year, make and model
	#does not account for ram 1500 etc TODO
	year = re.match(r'\d{4}',t).group(0)

	#year = "2010"
	make = "chevrolet"
	model = "equinox"

	#make = any(x in MAKES for c in t)#with makes being the list of all car makes
	#model = re.match()
	#print year.group()

	#make sure you initialize style
	#style = "None";
	#style would be sedan-4d

	#return year.group(), make, model, style
	return year, make, model#, style



"""
#opens initial kbb page
def getKBBPage(data):
	kbb = "https://www.kbb.com/"+data[1]+"/"+data[2]+"/"+data[0]+"/"
	thePage = urllib.request.urlopen(kbb)
	theSoup = BeautifulSoup(thePage, 'html.parser')
	#print theSoup
	newPage = theSoup.select("span[class=right] > p")
	newPage = newPage[0]

	if data[3] != "None":
		return "https://www.kbb.com"+newPage.a['href']+"&bodystyle="+style
	else:
		return "https://www.kbb.com"+newPage.a['href']

def nextPage(start):
	page = urllib.request.urlopen(start)
	soup = BeautifulSoup(page, 'html.parser')
	#data = soup.select("div[class=style-category-container] > div[class=mod-content__expanded-content]")
	#print soup
"""
file = open('output.txt','w')

#TODO
#opens the list of all car makes and models
#with open('car-list.json', 'r') as f:
#	data = json.load(f)

#for i in data:
#	print i

theLinks = getLinks()

#for e in theLinks:
	#returns year make and model in tuple in that order
	#data = iterate(e)
	#start = getKBBPage(data)

print (iterate(theLinks[0]))

"""
#returns year make and model in tuple in that order
data = iterate(theLinks[0])

#gets the first kbb page
start = getKBBPage(data)

#gets the next page
nextPage(start)

#note if this is a sedan or a coup. you must do some freaky deaky stuff
#that shall be done here

#otherwise it will continue on and take the cheapest option

#print data
"""







#file.write(str(soup))

file.close()
