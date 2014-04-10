#!/usr/bin/env python
# coding: utf-8

import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

# http://www.mkyong.com/python/how-do-send-email-in-python-via-smtplib/

def send_email_using_smtplib():
    to = 'test@exmaple.com'
    gmail_user = 'alazyer@gmail.com'
    gmail_pass = 'pass'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(gmail_user, gmail_pass)
    
    header = 'To: ' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject: Test\n'
    print header
    msg = header + '\n This is a test email from %s by using the Python:smtplib modu'
    server.sendmail(gmail_user, to, msg)

    print "Done!"
    server.close()

# http://www.oschina.net/code/snippet_153044_10826
def send_email():
    to = '790758591@qq.com'
    gmail_user = 'alazyer@gmail.com'
    gmail_pass = 'pass'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(gmail_user, gmail_pass)
    
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = to
    msg['Subject'] = "This is a test email"

    text = MIMEText("This is a test email, using the Python modules: smtplib, email")

    msg.attach(text)

    server.sendmail(gmail_user, to, msg.as_string())
    
    server.close()
    
if __name__ == '__main__':
    sys.exit(send_email())
