from code.games.game import *
from code .stages.maps import *
import code.clases as cl
import code.functions as m
import os
import json
import msvcrt
import main as c

class DetectarZonaGuardado:
    def __init__(self, playerData: object):
        self.playerData = playerData
    
    def DetecZona(self):
        if not self.playerData["lugarDeGuardado"]["lugar"] or len(self.playerData["lugarDeGuardado"]["lugar"]) == 0 and len(self.playerData["listaDeEventos"]) == 0:
            eve = cl.DarEvento("suenoInicial")
            eve.registrarEventoTemporal(c.tempPath)
            curPly = cargarTempDatos()
            os.system("cls")
            dreaming(curPly)
        else:
            if self.playerData["listaDeEventos"][-1] == "suenoInicial":
                os.system("cls")
                dreaming(self.playerData)
                
            if self.playerData["lugarDeGuardado"]["lugar"] == "casa" and self.playerData["listaDeEventos"][-1] == "introduccion":
                os.system("cls")
                intro(self.playerData)