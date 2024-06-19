# Copyright (c) 2024, Bruno Monteiro
# All rights reserved.
#

from lib.libmessage import *
from lib.liblog import *
from lib.libdb import *

db_instance = Db()

def getAllPlaces(table='pizzas', columns='*'):
        if table =='' or table == None:
            return default_invalid_field('"table"')
        if type(columns) == list:
            columns = ', '.join(columns)
        query = f"select {columns} from {table}"
        return db_instance.send_query(query)
    
# def getPlacesByUF():
    
def getPlacesUF(table="pizzas", columns='*',filters=None):
        if table =='' or table == None:
            return default_invalid_field('"table"')
        if type(columns) == list:
            columns = ', '.join(columns)
        query = f"select {columns} from {table} where uf={filters}"
        return db_instance.send_query(query)
    