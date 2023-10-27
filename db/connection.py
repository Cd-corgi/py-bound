import pymongo
import os
from code.functions import *
def establecerConexion(uri: str):
    try:
        cliente = pymongo.MongoClient(uri)
        return cliente
    except Exception as e:
        print("ERROR:\n", e)
        exit(0)