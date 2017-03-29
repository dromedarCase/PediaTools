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
