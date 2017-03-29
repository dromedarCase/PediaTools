#!/bin/python

import sys
import urllib.request

string = sys.argv[1]
language = sys.argv[2]

print ("Looking for string:", string)
print ("Wikipedia language:", language)

for line in sys.stdin:
    url = "http://" + language + ".wikipedia.org" + line
    
    page = urllib.request.urlopen(url)
    content = str(page.read())
    
    if content.find(string) != -1:
        print (url)
