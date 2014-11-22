# coding: utf-8

import os
import sys
import time
import requests
from requests.adapters import HTTPAdapter

fname = 'D:\\douban\\unPicId.txt'

LOST = open(os.path.dirname(fname) + '\\LOST.txt', 'w')

def getPic(fname):
    with open(fname) as f:
        lines = f.readlines()


    s = requests.Session()
    s.mount('http://', HTTPAdapter(max_retries=500))
    s.mount('https://', HTTPAdapter(max_retries=500))
    
    for line in lines[0:]:
        index = lines.index(line)
        bookid = line.strip().split('\n')[0]

        if bookid:
            book_url = 'https://api.douban.com/v2/book/%s' % bookid
            print '== For the %d item: (bookid, %s)' % (index, bookid),
            try:
                book_res = s.get(book_url)
                # print 'Finally get bookInfo, with status_code: %d' % book_res.status_code
            except:
                LOST.write('Index: ' + index + '; Id: ' + bookid + '; Reason: Failed to get the boonInfo with 500 time tries' + '\n')
                LOST.flush()
                continue

            if book_res.status_code == 200:
                book_json = book_res.json()
                book_title = book_json['title']
                print ',(book_title, <<%s>>).==' % book_title
            else:
                print ' =='
                print 'Failed to get bookInfowith a %d error.' % book_res.status_code
                LOST.write('Id: ' + bookid + '; Reason: get bookInfo response but with a !200 status_code.' + '\n')
                LOST.flush() 
                continue
            
            img_url = book_json['images']['medium']
            formation = img_url.split('.')[-1]
            print "Get the target Image url: %s" % img_url
            pname = os.path.join(os.path.dirname(fname), 'pic-unPicId/').replace('/', '\\') + 's%s.%s' % (bookid, formation)

            try:
                img_res  = s.get(img_url)
            except:
                LOST.write('Id: ' + bookid + '; Reason: Failed to get the image with 500 time tries' + '\n')
                LOST.flush()
                continue
            
            if img_res.status_code == 200:                
                content = img_res.content
                with open(pname, 'wb') as p:
                    p.write(content)
                print "Saved the Image with fname: %s" % pname
                print 'Well done. Get image correctly for item %d in formation %s!'  % (index, formation)
            else:
                print 'Failed to get image with a %d error.' % img_res.status_code
                LOST.write('Id: ' + bookid + '; Reason: get imageContent response but with a !200 status_code.' + '\n')
                LOST.flush()
                print 
                continue
            print 
            time.sleep(7)
    s.close()       

if __name__ == '__main__':
    getPic(fname)
