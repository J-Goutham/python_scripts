#!/usr/bin/python

import datetime as date
import os
import sys

try:
    url = sys.argv[1]
    file = sys.argv[2]

    print ("\n")
    date = date.datetime.now()

    print ("Starting at %s" % date)
    print ("\n")
    print ("="*30)
    print ("url: %s" % url)
    print ("Method: GET")
    print ("negative_stauts: 404")
    print ("wordlist: %s" % file)
    print ("="*30)
    print ("\n")

    code=(f"""for i in $(cat {file}); do code=$(curl -X GET -m 1 -s -I {url}/$i -H "User-Agnet : Anonymous" | head -n1 | egrep '[0-9]' | cut -d' ' -f2); echo "/$i  status:($code)"; done | grep -v 404""")
    os.system(code)

except IndexError:
    print (f"Syntax: python {sys.argv[0]} <url> <wordlist>")

except KeyboardInterrupt as K:
    print ("\nProcess Stopped!")
    print (f"Finishing at {date}")
