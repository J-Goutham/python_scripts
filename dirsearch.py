#!/usr/bin/python

import requests
import sys
from os import system

target = sys.argv[1]
text = open(sys.argv[2], 'r').readlines()

tar = (target).split('/')

length = len(text)

print ('\n\a\n\033[92mBruteForcing Directory....\n')
print ("-"*30)
print (f'method: Get\nWordlist: {length}\nTarget: {target}\nNegative_statuscode:404')
print ("-"*30+"\n")

try:
    for list in text:
        word = list.strip()
        full_url = target + "/" + word
        req = requests.get(url=full_url, allow_redirects=True, timeout=5)
        code = (str(req.status_code))
        if code == '404':
            continue
        print ('\n\033[96m/'+word, f'({code})')

except KeyboardInterrupt as k:
    print ('\n\033[91mProcess Stopped!')

