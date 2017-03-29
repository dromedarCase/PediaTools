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

items = []
pointer = 1

while True:
    pointer = ul.find('">', pointer) + 2
    if pointer == 1:
        break
    end = ul.find('<', pointer)
    
    items.append(ul[pointer:end])
    
print (str(items));
