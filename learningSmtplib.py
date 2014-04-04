#!/usr/bin/env python
# coding: utf-8

import sys
import smtplib

# http://www.mkyong.com/python/how-do-send-email-in-python-via-smtplib/

def send_email_using_smtplig():
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

if __name__ == '__main__':
    sys.exit(send_email_using_smtplib())
