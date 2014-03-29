#!/usr/bin/env python
# coding: utf-8

import socket


# http://stackoverflow.com/questions/10748959/get-hostname-from-ip-address
def getHost():
    subnet = '192.168.0.%d'

    for i in xrange(1, 255):
        ip = subnet % i
        try:
            print socket.gethostbyaddr(ip)  # [name, aliaslist, iplist]
        except:
            print "No host posses %s" % ip
