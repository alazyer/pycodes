#!/usr/bin/env python
# coding: utf-8

import logging
import os

def basic():
    logging.basicConfig(filename=os.path.join(os.getcwd(), 'log.txt'), \
        level = logging.DEBUG, filemode='w', format='%(asctime)s - %(levelname)s: %(message)s')

    logging.debug("This is a debug message")
    logging.info("This is a info message")
    logging.warning("Thisi is a warning message")
    logging.error("This is a error message")
    logging.critical("This is a critical message")

    logging.shutdown()

if __name__ == '__main__':
    basic()
