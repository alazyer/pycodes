#!/usr/bin/env python
# coding: utf-8

import re
import sys
import requests

def requestsPrepare():
    s = requests.Session()
    s.mount('http://', requests.adapters.HTTPAdapter(max_retries=5))
    s.mount('http://', requests.adapters.HTTPAdapter(max_retries=5))
    
    return s
    
def getData():
    if len(sys.argv) == 3:  
        login_email = sys.argv[1]
        login_password = sys.argv[2]
        return (login_email, login_password)
    else:
        print "Usage:"
        print "python doubanLogin.py login_email login_password"
        sys.exit()

def login(login_url, login_email, login_password): 

    s = requestsPrepare()
    
    data = {'form_email': login_email, 'form_password': login_password, 'source': 'index_nav'}

    res = s.post(login_url, data=data)

    if res.url == login_url:
        html = res.text
        imgurl = re.search('<img id="captcha_img" src="(.+?)" alt', html)
    
        if imgurl:
            url = imgurl.group(1)
            with open('~/Pictures/douban_validation.jpg', 'wb') as f:
                f.write(s.get(url).content)
            captcha = re.search('<input type="hidden" name="captcha-id" value="(.+?)"/>'  , html)
            captcha = captcha.group(1)

            if captcha:
                vcode = raw_input('请您输入图片上的验证码: \n.Help: 图片位置: ~/Pictures/douban_validation.jpg')
                data['capcha-solution'] = vcode
                data['capcha-id'] = captcha
                data['user_login'] = '登录'
                res = s.post(login_url, data=data)
    
                if res.url == 'http://www.douban.com':
                    print "login successly with the validation code"
                    return s
                else:
                    return s
                    print "Something wrong! Try again later, please"
            else:
                return s
                print "Failed to parse the captcha image id for validation! Please try again later."
        else:
            return s
            print "Failed to parse the captcha image url to download the image! Please try again later."
            
    elif res.url == 'http://www.douban.com':
        print "login successly without validation code"
        return s
    else:
        return s
        print "Something wrong! Try again later, please"

if __name__ == '__main__':
    login_url = "https://www.douban.com/accounts/login"
    login_email, login_password = getData()
    login(login_url, login_email, login_password)
