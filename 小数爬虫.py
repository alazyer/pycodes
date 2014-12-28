#!/usr/bin/env python
# --*-- coding: utf-8 --*--

import os
import requests
from bs4 import BeautifulSoup

base_url = 'http://www.23wx.com/html/32/32925/%s'

def get_book(base_url, first_page):
    f = open('test.txt', 'w')

    first_url = base_url % first_page
    title, main, next = get_page(first_url)
    print "Got ", title
    f.write(u'和表姐同居的日子\n')
    f.write(title)
    f.write('\n')
    f.write(main)
    f.write('\n')

    next = False

    while next:
        title, main, next = get_page(base_url % next)
        print "Got ", title
        f.write(title)
        f.write('\n')
        f.write(main)
        f.write('\n')

def get_page(page_url):
    print page_url
    content = requests.get(page_url).content
    soup = BeautifulSoup(content)
    print 'footlink' in content

    main_dd = soup.find('dd', {'id': 'contents'})
    h_next = main_dd.findPrevious('h3')

    main = main_dd.text.encode('utf-8')
    title = main_dd.findPrevious('h1').text.encode('utf-8')
    try:

        next = h_next.findChildren('a')[-1]['href']
    except:
        next = None
    return (title, main, next)

if __name__ == '__main__':
    get_book(base_url, '17781659.html')
