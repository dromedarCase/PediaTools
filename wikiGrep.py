#!/bin/python

import sys
import urllib.request

string = sys.argv[1]
language = sys.argv[2]

print ("Looking for string:", string, file=sys.stderr)
print ("Wikipedia language:", language, file=sys.stderr)
print (file=sys.stderr)

for line in sys.stdin:
    url = "http://" + language + ".wikipedia.org" + line
    
    page = urllib.request.urlopen(url)
    content = str(page.read())
    
    if content.find(string) != -1:
        print (url)
