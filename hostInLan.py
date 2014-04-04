#!/usr/bin/env python
# coding: utf-8

import sys
import socket
import threading

# http://stackoverflow.com/questions/10748959/get-hostname-from-ip-address

def getHost(ip):
    try:
        print 
        print socket.gethostbyaddr(ip)  # [name, aliaslist, iplist]
        print 
    except:
        pass

def main():
    threads = []
    ip = '192.168.0.%d'
    for i in xrange(1, 255):
        t = threading.Thread(target=getHost, args=((ip % i, )))
        threads.append(t)

    for t in threads:
        t.start()

if __name__ == '__main__':
    sys.exit(main())
