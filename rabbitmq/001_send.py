#!/usr/bin/env python
# encoding: utf-8

from __future__ import print_function
import pika


def send():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost')
    )

    channel = connection.channel()

    channel.queue_declare(queue='hello')

    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello World!')

    print(" [x] Sent 'Hello World!'")

    connection.close()

if __name__ == '__main__':
    send()
