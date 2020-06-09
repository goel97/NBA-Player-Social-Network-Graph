
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

start_time = time()

players = np.loadtxt("links.txt",dtype = str)
print(players)
for j in range(100,1000,20):
	requests = j
	for link in players[j:j+20]:
		try:
			url_player=urlopen(link)
			sleep(randint(3,10))

			requests = requests + 1
			elapsed_time = time() - start_time
			print('Request:{}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))
			clear_output(wait = True)

			player = BeautifulSoup(url_player, "html.parser")
			f=open("data.txt", "a+")
			text = ""

			# stripping <script> tags from html
			for script in player.find_all("script"):
			  player.script.extract()

			# extracting text from html paragraphs
			for para in player.find_all("p"):
			  if text == "":
			    text = para.get_text()
			  else:
			    text = text + "\n\n" + para.get_text()

			# removing wiki-references
			text = re.sub(r'\[\d+\]', "", text)

			f.write(text)
		except:
			pass
	sleep(randint(50,60))
	
f.close()