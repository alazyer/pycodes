#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2
import MySQLdb


DB_MODULES = {
    'postgres': psycopg2,
    'mysql': MySQLdb
}

class BaseDbClient(object):
    engine = None

    def get_connection_kwargs(self):
        raise NotImplementedError('subclasses of DbClient may require a get_connection_params() method')

    def get_connection(self):
        if self.engine not in DB_MODULES:
            raise Exception(
                "Unsupported Db Engine, currently only support %s",
                ', '.join(DB_MODULES.keys()))

        db_module = DB_MODULES.get(self.engine)
        kwargs = self.get_connection_kwargs()

        return db_module.connect(**kwargs)

    def get_cursor(self):
        conn = self.get_connection()

        return conn.cursor()

    def execute(self, sql):
        return self.get_cursor().execute(sql)
