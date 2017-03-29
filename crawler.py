#!/bin/python

import sys
import urllib.request 

category = sys.argv[1]
language = sys.argv[2]

print ("Crawling category:", category, file=sys.stderr)
print ("Wikipedia language:", language, file=sys.stderr)

url = "http://"+language+".wikipedia.org/wiki/Category:"+category
print ("URL:", url, file=sys.stderr)
print (file=sys.stderr)

while url.find(" ") == -1:
    categoryPage = urllib.request.urlopen(url)

    content = str(categoryPage.read())

    mainContentBegin = content.find("mw-pages")
    mainContendEnd = content.find("<noscript>", mainContentBegin)
    mainContent = content[mainContentBegin:mainContendEnd]

    items = []

    ulBegin = mainContent.find("<ul>") + 4
    while ulBegin != 3:
        ulEnd = mainContent.find("</ul>", ulBegin)

        ul = mainContent[ulBegin:ulEnd]

        subitems = []
        pointer = 1

        pointer = ul.find('href="', pointer) + 6
        while pointer != 5:
            end = ul.find('"', pointer)
            subitems.append(ul[pointer:end])
            pointer = ul.find('href="', pointer) + 6
        
        items.extend(subitems)
        ulBegin = mainContent.find("<ul>", ulBegin) + 4
        
    for item in items:
        print (item)
        
    # looking for next page

    pointer = mainContent.find(") (") + 3
    end = mainContent.find(")", pointer)
    link = mainContent[pointer:end]

    pointer = link.find('href="') + 6
    end = link.find('#', pointer)
    link = link[pointer:end].replace("&amp;","&")

    url = "http://"+language+".wikipedia.org"+link
