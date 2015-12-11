# coding: utf-8

import os
import time
import pickle
import requests
from PIL import Image
from StringIO import StringIO
from requests.adapters import HTTPAdapter

fname = os.path.dirname(__file__) + '/book.txt'

LOST = dict()

def getPic(fname):
    with open(fname) as f:
        lines = f.readlines()


    s = requests.Session()
    s.mount('http://', HTTPAdapter(max_retries=500))
    s.mount('https://', HTTPAdapter(max_retries=500))
    
    for line in lines[1437:]:
        index = lines.index(line),
        print 'For the %d item:============>' % index
        
        bookid = line.strip().split('\n')[0]
        if bookid:
            book_url = 'https://api.douban.com/v2/book/%s' % bookid
            fname = os.path.join(os.path.dirname(__file__), os.pardir, 'pic') +'s%s.jpg' % bookid
            try:
                book_res = s.get(book_url)
                print 'Finally get bookInfo, with status_code: %d' % book_res.status_code
            except:
                LOST[index] = 'Failed to get the bookInfo with 500 times try.'
                continue
            
            book_json = book_res.json()
            img_url = book_json['images']['medium']

            j = 0
            try:
                img_res  = s.get(img_url)
                print 'Finally try get imgContent, with status_code: %d' % img_res.status_code
            except:
                LOST[index] = 'Get bookInfo correctly, but failed to get imgContent with 500 times try'
                continue
                    
            content = img_res.content
            img = Image.open(StringIO(content))
            img.save(fname)
            print 'Well done. Get image correctly for item %d!'  % index
            print 
            time.sleep(7)
    s.close()       
    pickle.dump(LOST, open(os.path.dirname(__file__) + 'LOST.p'), 'w')

if __name__ == '__main__':
    getPic(fname)
