# NBA-Player-Social-Network-Graph

Implemented a NLP problem to automate the Entity-Relation Graph generated from an unstructured text, also developed an interactive visualization graph which can be used for search and recommendations. 

* The entity-relation graph is built from free-text extracted from Wikipedia articles, and shows relations between various players, awards, teams or Tournaments using Stanford’s Core-NLP library algorithms.
* Used D3.js to create an interactive visualization graph which can be used in search, recommendation applications. 

FOR OUTPUT OPEN GRAPH1.HTML OR GRAPH2.HTML

## FOR DATA SCRAPING

	python web_scrape.py https://en.wikipedia.org/wiki/Lists_of_National_Basketball_Association_players
	
	#saves player links in files links.txt
	
	python scrape_players.py/allstarts.py
	
	#extracts text from links.txt and append in new doc/extracts with a heading

## FOR ENTITY RELATION GRAPH

	directory-> Stanford-OpenIE-Python
	python main.py -f input.txt -g
	Will generate a [GraphViz DOT](http://www.graphviz.org/) graph and its related PNG file in `/tmp/openie/`
	and a output.txt file with all the extracted relations

		open out.dot file in text editor and copy paste data into a new text file relation.txt
		sed "s/;/;\n/g" relation.txt > foo_Out.txt
		#show each relation in new line
		convert foo_Out.txt to required .json file in format same as player.json

		OR

		convert the tab separated file (output.txt) to to required .json file in format same as player.json
			(format of tsv -> entity[1]	Label	entity[2])

	add images in images folder and add their path to Entity_relation_graph.html/graph1.html/graph2.html


## UTILITIES

>	use python duplicate_lines.py to remove duplicate relations from foo_Out.txt


## FILE DIRECTORY

* images 
	- contains the images for node icons
* allstarscrape.py 
	- extract the wikilinks from allstarlinks.txt and append the data to allstarsdata.txt
* web_scrape.py 
	- extract links for all the nba players (around 4500) and append those links to links.txt
* scrape_players.py
	- take wikilinks from links.txt and append text for each player in data.txt
* Standford-OpenIE-Python 
	- directory which contain the python wrapper for relation extraction. 	
	input.txt - The input file containing text data. (copy paste the text from data.txt here)
	allstarsdata.txt - The input file containing text data for allstars team players 
	output.txt - Tab separated Ouput File
	standford-openie - contaisn the java api for standford-corenlp-openie
* relation.txt
	 - contains data in text format from out.dot file (created in home/tmp/openie)
* foo_Out.txt
	 - same as relation.txt but has each relation in separate line
* player.json
	 - file with the entity-relations in the format required by d3
* graph1.html 
	- output of graph with node icons as images
* Entity_relation_graph.html/graph2.html 
	- output of graph with node icons filled with colours accordingly if they are place, player, tittle/award, team. and display node images on mouseover


