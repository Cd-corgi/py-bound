from code.games.game import *
from code .stages.maps import *
from code.clases import *
import code.functions as m
import os
import json
import msvcrt
import main as c

class DetectarZonaGuardado:
    def __init__(self, playerData: object):
        self.playerData = playerData
    
    def DetecZona(self):
        if not self.playerData["lugarDeGuardado"]["lugar"] or len(self.playerData["lugarDeGuardado"]["lugar"]) == 0:
            
            pass