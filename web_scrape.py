 # importing libraries
 # usage python web_scrape.py https://en.wikipedia.org/wiki/Lists_of_National_Basketball_Association_players
from bs4 import BeautifulSoup
from urllib.request import urlopen
import importlib
import re
import sys
import numpy as np

from time import sleep
from random import randint
from time import time


from IPython.core.display import clear_output
from warnings import warn

web_url = sys.argv[1]
page = urlopen(web_url)
wiki = BeautifulSoup(page, "html.parser")

start_time = time()
requests = 0

links = []
#f=open("data.txt", "a+")
let=wiki.find('div', class_ = 'toc plainlinks hlist')
for link in let.find_all('a'):
	if link.has_attr('href'):
		links.append(link.attrs['href'])
mystring = "https://en.wikipedia.org"
links = [mystring + s for s in links]

players = []

for link in links:
	url=urlopen(link)
	webpage = BeautifulSoup(url, "html.parser")
	leta=webpage.find('div', class_ = 'div-col columns column-width')
	for link_1 in leta.find_all('a'):
		if link_1.has_attr('href'):
			players.append(link_1.attrs['href'])

mystring = "https://en.wikipedia.org"
players = [mystring + s for s in players]
#link_list = open("links.txt","a+")
np.savetxt("links.txt",np.asarray(players),fmt="%s")
print(*links, sep = "\n")

print(*players, sep = "\n")
print (len(players))
print (len(links))
