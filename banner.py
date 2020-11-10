#!/usr/bin/python

import socket, sys

def retban():
    try:
        ip = sys.argv[1]
        port = sys.argv[2]
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        print (s.recv(1024))
    except:
       pass

retban()
