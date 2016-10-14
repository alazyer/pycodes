#!/usr/bin/env python
# encoding: utf-8

from __future__ import print_function
import pika
import sys


def receive():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost')
    )

    channel = connection.channel()

    channel.exchange_declare(exchange='direct_logs',
                             type='direct')

    result = channel.queue_declare(exclusive=True)
    queue_name = result.method.queue

    severities = sys.argv[1:]
    if not severities:
        sys.stderr.write('Usage: %s [info] [waring] [error]\n' % sys.argv[0])

    for severity in severities:
        channel.queue_bind(exchange='direct_logs',
                           queue=queue_name,
                           routing_key=severity)

    print(' [*] Waiting for messages. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        print(" [x] Received channel: ", ch)
        print(" [x] Received method: ", method)
        print(" [x] Received properties: ", properties)
        print(" [x] Received message routing_key: %r" % method.routing_key)
        print(" [x] Received body: %r" % body)

    channel.basic_consume(callback,
                          queue=queue_name,
                          no_ack=True)

    channel.start_consuming()


if __name__ == '__main__':
    receive()
