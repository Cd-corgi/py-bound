import msvcrt as keyb
import os
from colorama import *
import json
from code.clases import *
from code.stages.maps import *
import code.functions as contar


def cargarTempDatos():
    with open('./code/temp/currentP.json') as file:
        data = json.load(file)
    return data

def intro(playerData):
    if playerData["listaDeEventos"][-1] == "introduccion":
        epi1 = EscenarioCasa(playerData)
        epi1.EleccionRutas()
        contar.anyKey2Continue()
    else:
        print("Error: No deberias estar aqui")
        print("Lefting Event!")
        exit(0)

def dreaming(playerData):
    if playerData["listaDeEventos"][-1] == "suenoInicial":
        yes = EscenarioSueno(playerData)
        yes.AvanzarRuta()
        contar.anyKey2Continue()
        newPD = cargarTempDatos()
        intro(newPD)
    else:
        print("Error: No deberias estar aqui")
        print("Lefting Event!")
        exit(0)

def mGame():
    os.system("cls")
    if os.path.isfile('./code/temp/currentP.json'):
        dat = cargarTempDatos()
        n = contar.loadNPCDialog('Ana', 0)
        i = 0
        while i < 2:
            print(n["dialogos"][i].replace(
                "{player}", dat["nombre"]).replace("{likes}", dat["gusto"]))
            i += 1
        i = 0
        contar.setTimeout(0.3)
        contar.anyKey2Continue()
        os.system("cls")
        contar.setTimeout(0.5)
        print("Sientes que un frio misterioso te rodea y todo a tu alrededor se congela al punto de volverte un tempano", end="")
        contar.puntsus(0.5)
        contar.anyKey2Continue()
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
