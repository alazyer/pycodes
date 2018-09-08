#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import BaseDbClient


class DbClient(BaseDbClient):
    engine = 'mysql'

    def get_connection_kwargs(self, db_name=None):
        kwargs = dict(
            host=os.getenv('DB_HOST', 'localhost'),
            port=os.getenv('DB_PORT', 3306),
            user=os.getenv('DB_USER', 'root'),
            passwd=os.getenv('DB_PASSWORD', '123456')
        )
        if db:
            kwargs['db'] = db_name

        return kwargs
