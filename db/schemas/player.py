import pymongo
import os
import json

def Pschema():
    PlayerSchema = {
        "name": {'type': 'string'},
        "genero": {'type': 'string'},
        "gusto": {'type': 'string'},
        "color": {'type': 'int'},
        "combate": {'type': 'int'},
        "inventario": [{
            "nombre": {'type': 'string'},
            "cantidad": {'type': 'int'}
        }],
        "estadistica": {
            "xp": { 'type': 'int', 'default': 0 },
            "limiteXP": { 'type': 'int', 'default': 50 },
            "nivel": { 'type': 'int', 'default': 1 },
            "ataque": { 'type': 'int', 'default': 5 },
            "defensa": { 'type': 'int', 'default': 5 },
            "vida": { 'type': 'int', 'default': 25 },
        },
        "lugarDeGuardado": {
            "lugar": { 'type': 'string' },
            "zona": { 'type': 'string' },
        },
        "listaDeEventos": [{}]
    }
    
    return PlayerSchema