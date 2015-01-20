#!/usr/bin/env python
# coding: utf-8

import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

# http://www.mkyong.com/python/how-do-send-email-in-python-via-smtplib/

def send_email_using_smtplib(mail_server, port, from_user, from_password, to_user):
    to_user = to_user
    from_user = from_user
    from_password = from_password

    server = smtplib.SMTP(mail_server, port)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(from_user, from_password)

    header = 'To: ' + to_user + '\n' + 'From: ' + from_user + '\n' + 'Subject: Test\n'
    print header
    msg = header + '\n This is a test email from %s by using the Python:smtplib modu'
    server.sendmail(from_user, to_user, msg)

    print "Done!"
    server.close()

# http://www.oschina.net/code/snippet_153044_10826
def send_email_multipart(mail_server, port, from_user, from_password, to_user, image_file_path):
    to_user = to_user
    from_user = from_user
    from_password = from_password

    server = smtplib.SMTP(mail_server, port)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(from_user, from_password)

    msg = MIMEMultipart()
    msg['From'] = from_user
    msg['To'] = to_user
    msg['Subject'] = "This is a test email"

    text = MIMEText("This is a test email, using the Python modules: smtplib, email")
    msg.attach(text)

    image = MIMEImage(open(image_file_path, 'rb').read())
    image.add_header("Content-ID", "<image1>")

    msg.attach(image)

    server.sendmail(from_user, to_user, msg.as_string())

    server.close()

if __name__ == '__main__':
    sys.exit(send_email())
