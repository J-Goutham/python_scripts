#!/usr/bin/python

import os
import socket
import sys
import requests
import time
import json

os.system('clear')

like = open(sys.argv[2], 'r+')

class Color:
    green = '\033[92m'
    yellow = '\033[93m'
    blue = '\033[94m'
    pink = '\033[95m'
    red = '\033[91m'
    cyan = '\033[96m'

try:
    get = sys.argv[1]
    put = get.split('/')[-1]
    print (Color.red+'\nChecking.....\n')
    s = socket.gethostbyname(put)
    print (Color.green+'IP: {}\n'.format(s))


    def dirb():
        print("Searching directory......")
        os.system("command -v gobuster >/dev/null 2>&1 || go get github.com/OJ/gobuster; cd go/bin; ")
        os.system(f"gobuster dir -u {get} -w $HOME/../usr/share/dirb/wordlists/common.txt -q")
        print ("Fininded directory....")

    def robots():
        time.sleep(1)
        print (Color.cyan+'[ Searching robots.txt....] \n')
        start = requests.get(url=get, params='robots.txt').url
        do = start.split('?')
        stop = ''.join(do)
        abuse = requests.get(stop).content
        if b'</html>' in abuse:
            print (Color.red+'file not found....\n'.title())
        else:
            print (Color.yellow+f'File Found:\n{abuse.decode()}')
    def Scan():
        print (Color.red+'\n[ Scanning ports....] \n')
        os.system(f"nmap {put} | grep open")

    def http():
        print (Color.cyan+'\n[ http headers ]\n')
        req = requests.get(url=get).headers
        for k in req.keys():
            print (Color.green+k, ':', req[k])

    def Geoip():
        print (Color.cyan+'\n[ geo_ip ]\n'.title())
        r = requests.get('http://ipinfo.io/{}'.format(s))
        obj = json.loads(r.text)
        for i in obj.keys():
            print(Color.green+i, ':', obj[i])
    def FindDir():
        print ("\033[96m \n[ BruteForecing..... ] \n")
        fun = (f"""for i in `cat {like}`; do code=$(curl -s -I {get}/$i | head -n 1| egrep '[0-9]' | cut -d ' ' -f2); var="$i"; echo "$var  status: $code"; done""")
        os.system(fun)

except requests.exceptions as i:
    print ('connection error'.title())

def b():
    pass

if __name__ == '__main__':
    robots()
#    Scan()
    http()
    Geoip()
    FindDir()

