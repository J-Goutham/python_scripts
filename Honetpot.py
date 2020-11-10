#!bin/python

import socket
import os
import time
import argparse
import sys
from termcolor import *
import threading

parser = argparse.ArgumentParser()
parser.add_argument('--ip', '--ip_adrress', dest='ip',   required=True, help='Used to mention ip')
args = parser.parse_args()

ip = args.ip
time.sleep(1)
os.system("clear")
print (colored("[•]Honeypot Started.....", 'yellow'))


def pot():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((ip, 80))
        s.listen(80)
        while True:
            client_con,client_addr = s.accept()
            os.system(f'nmap {client_addr[0]} > honey.log')
            print ("Visiter Found ![{}]".format(client_addr[0]))
            client_con.send(b"\t\t<h1>$You Has Been Hacked!!</h1>\nK5LTSMKJIU2XMYRSJFFQU===")
            data = client_con.recv(10024)
            print ('\n\033[92m'+data.decode('utf-8'))

    except KeyboardInterrupt as g:
        print (colored("\nHoneypot Stopped!!", 'blue'))
        sys.exit()
        s.close()
    except PermissionError as P:
        print (colored('Run as root', 'red'))
        sys.exit()
    except ConnectionResetError as E:
        print (colored(f'[{client_addr[0]}]  This ip Scanned with Nmap', 'red'))
        t1 = threading.Timer(1, pot)
        t1.start()
    except OSError as Os:
        time.sleep(1)
        s.close()
    finally:
        s.close()

if __name__ == "__main__":
    while True:
        pot()
