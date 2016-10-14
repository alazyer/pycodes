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

    channel.queue_declare(queue='task_queue', durable=True)

    message = ' '.join(sys.argv[1:]) or 'Hello World!'

    channel.basic_publish(exchange='',
                          routing_key='task_queue',
                          body=message,
                          properties=pika.BasicProperties(
                              delivery_mode=2
                          ))

    print(" [x] Sent %r" % message)

    connection.close()

if __name__ == '__main__':
    send(sys)
