#!/usr/bin/env python
# coding: utf-8

##################################################
#### get the physical add of ip/domain
#### following 'blog.imsuzie.com/archives/751'
##################################################

import re
import sys
import json
import socket
import requests

if __name__ == '__main__':
    if len(sys.argv) == 2:
        domain = sys.argv[1]

        domain = re.sub(r'(http|https)://', '', domain)
        domain = re.sub(r'/(.*)', '', domain)
        result = socket.getaddrinfo(domain, None)
        ip = result[0][4][0]
        url = 'http://ip.taobao.com/service/getIpInfo.php?ip=' + ip
        res = requests.get(url)
        info = res.json()
        if re.findall(r'\d+.\d+.\d+.\d+', domain):
            domain = ''
        if info['data']:
            print domain, ip, info['data']['country'], info['data']['region'], info['data']['city'], info['data']['isp']
        else:
            print domain, ip
    else:
        print "Usage():"
        print "python ip.py www.nuist.edu.cn|http://www.nuist.edu.cn|202.195.224.88"
        sys.exit(2)
