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

    channel.exchange_declare(exchange='direct_logs',
                             type='direct')

    severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
    message = ' '.join(sys.argv[2:]) or 'Hello World!'

    channel.basic_publish(exchange='direct_logs',
                          routing_key=severity,
                          body=message)

    print(" [x] Sent %r: %r" % (severity, message))

    connection.close()

if __name__ == '__main__':
    send(sys)
