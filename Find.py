#!/data/data/com.termux/files/usr/bin/python

import requests
import sys
import time
import os


class Find:
    os.system('clear')
    print ('Checking...')
    time.sleep(1)
    url = sys.argv[1]
    headers = {'User-Agent':'Anonymous'}
    s=requests.head(url, allow_redirects=True, headers=headers).url
    try:
        a = (url)
        print ("")
        print (f"Url>> {s}")
        sys.exit()
    except IndexError as I:
        print ("Usage: ./unshorten.py <Url>")
        sys.exit()

#obj = Find()
