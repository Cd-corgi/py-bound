import pymongo
from pymongo.server_api import ServerApi
import dns.resolver
import os
from code.functions import *

dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']

def establecerConexion(uri: str):
    try:
        cliente = pymongo.MongoClient(uri, server_api=ServerApi('1'))
        return cliente
    except Exception as e:
        raise e