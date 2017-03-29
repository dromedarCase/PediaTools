#!/bin/python

import sys
import urllib.request 

category = sys.argv[1]
language = sys.argv[2]

print ("Crawling category:", category)
print ("Wikipedia language:", language)

url = "http://"+language+".wikipedia.org/wiki/Category:"+category
print ("URL:", url)
categoryPage = urllib.request.urlopen(url)

content = str(categoryPage.read())

ulBegin = content.find("<ul>", content.find("<ul>") + 1) + 4
ulEnd = content.find("</ul>", ulBegin)

ul = content[ulBegin:ulEnd]

print (ul)
