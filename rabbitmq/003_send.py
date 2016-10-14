#!/usr/bin/env python
# encoding: utf-8

from __future__ import print_function
import pika
import sys


def send(sys):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost')
    )

    channel = connection.channel()

    channel.exchange_declare(exchange='logs',
                             type='fanout')

    message = ' '.join(sys.argv[1:]) or 'info: Hello World!'

    channel.basic_publish(exchange='logs',
                          routing_key='',
                          body=message)

    print(" [x] Sent %r" % message)

    connection.close()

if __name__ == '__main__':
    send(sys)
