from code.functions import *
import msvcrt as keyb
import os
from colorama import *
import json
from code.clases import *
from code.stages.maps import *


def cargarTempDatos():
    with open('./code/temp/currentP.json') as file:
        data = json.load(file)
    return data

def dreaming(playerData):
    if playerData["listaDeEventos"][-1] == "suenoInicial":
        yes = EscenarioSueno(playerData)
        yes.AvanzarRuta()
        anyKey2Continue()
    exit(0)
    
def mGame():
    os.system("cls")
    if os.path.isfile('./code/temp/currentP.json'):
        dat = cargarTempDatos()
        npc = loadNPCDialog('Ana', 0)
        i = 0
        while i < 2:
            print(npc["dialogos"][i].replace("{player}", dat["nombre"]).replace("{likes}", dat["gusto"]))
            i += 1
        i = 0
        setTimeout(0.3)
        anyKey2Continue()
        os.system("cls")
        setTimeout(0.5)
        print("Sientes que un frio misterioso te rodea y todo a tu alrededor se congela al punto de volverte un tempano", end="")
        puntsus(0.5)
        anyKey2Continue()
        eve = DarEvento("suenoInicial")
        eve.registrarEventoTemporal('./code/temp/currentP.json')
        newDat = cargarTempDatos()
        dreaming(newDat)
        os.system("cls")
        if newDat["listaDeEventos"][-1] == "suenoInicial":
            dreaming(newDat)
    else:
        print("An error just ocurred... There's no player or nor player name have beed registered...")
        setTimeout(3)
        os.system("exit()")
    return