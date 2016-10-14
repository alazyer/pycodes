#!/usr/bin/env python
# encoding: utf-8

from __future__ import print_function
import time
import pika


def receive():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost')
    )

    channel = connection.channel()

    channel.queue_declare(queue='task_queue', durable=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        print(" [x] Received channel: ", ch)
        print(" [x] Received method: ", method)
        print(" [x] Received properties: ", properties)
        print(" [x] Received body: %r" % body)
        time.sleep(body.count(b'.'))
        print(' [x] Done')
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(callback,
                          queue='task_queue')

    channel.start_consuming()


if __name__ == '__main__':
    receive()

# ### sample result ###

# [*] Waiting for messages. To exit press CTRL+C
# [x] Received channel:  <pika.adapters.blocking_connection.BlockingChannel object at 0x7f879cc673d0>
# [x] Received method:  <Basic.Deliver(['consumer_tag=ctag1.165dd5ce5c1d4a978307e48aed037fa5', 'delivery_tag=1', 'exchange=', 'redelivered=False', 'routing_key=hello'])>
# [x] Received properties:  <BasicProperties>
# [x] Received body: 'Hello World!'
