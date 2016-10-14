#!/usr/bin/env python
# encoding: utf-8

from __future__ import print_function
import pika


def receive():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost')
    )

    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(" [x] Received channel: ", ch)
        print(" [x] Received method: ", method)
        print(" [x] Received properties: ", properties)
        print(" [x] Received body: %r" % body)

    channel.basic_consume(callback,
                          queue='hello',
                          no_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    receive()

# ### sample result ###

# [*] Waiting for messages. To exit press CTRL+C
# [x] Received channel:  <pika.adapters.blocking_connection.BlockingChannel object at 0x7f879cc673d0>
# [x] Received method:  <Basic.Deliver(['consumer_tag=ctag1.165dd5ce5c1d4a978307e48aed037fa5', 'delivery_tag=1', 'exchange=', 'redelivered=False', 'routing_key=hello'])>
# [x] Received properties:  <BasicProperties>
# [x] Received body: 'Hello World!'
