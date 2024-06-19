# Copyright (c) 2024, Bruno Monteiro
# All rights reserved.
#
"""
Library to interact with a PostgreSQL database using psycopg2.
"""

import psycopg2
from lib.libmessage import *
from lib.liblog import *

def read_db_config(filename='db.config'):
    """
    Reads a configuration file and returns a dictionary with the configuration
    parameters.

    Args:
        filename (str, optional): Name of the configuration file. Defaults to
        'db.config'.

    Returns:
        dict: A dictionary with the configuration parameters.
    """
    config = {}
    with open(filename, 'r') as f:
        for line in f:
            key, value = line.strip().split('=')
            config[key] = value
    return config


log = liblog()
config = read_db_config()


class Db:
    """
    Class to interact with a PostgreSQL database using psycopg2.
    """
    def __init__(self):
        """
        Initializes the class with the database configuration parameters.
        """
        self.host = config['host']
        self.database = config['database']
        self.user = config['user']
        self.password = config['password']

    def send_query(self, query):
        """
        Sends a query to the database and returns the result.

        Args:
            query (str): The SQL query to be executed.

        Returns:
            list: A list of tuples with the query result.
        """
        log.info('Connecting to DB')
        with psycopg2.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password
        ) as conn:
            log.info('Connected')
            with conn.cursor() as cur:
                cur.execute(query)
                rows = cur.fetchall()
                log.info(rows)
                cur.close()
                log.info('Connection closed!')
        return rows

