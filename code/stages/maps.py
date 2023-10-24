import os
import json
from code.functions import *
from code.clases import *


class EscenarioSueno:
    def __init__(self, playerData: object):
        self.playerData = playerData
        self.escenarios = [
            "En un bosque helado, está rodeado de arboles enpinados. Hay un camino que te lleva solo hacia adelante... Solo puedes avanzar.",
            "Vas en la mitad de la ruta y sientes que este frio te abraza sin piedad... Tus manos y piernas se sienten rigidas. Solo puedes avanzar.",
            "Llegas a un punto donde el frio te gana y no puedes seguir caminando. Un viento murmulla tu nombre y te hace esta pregunta:\n\n¿A quien le temes?"
        ]
        self.mobsChance = 0
        self.mobs = []
        self.idx = 0

    def AvanzarRuta(self):
        while self.idx < len(self.escenarios):
            if self.idx - 1 == len(self.escenarios):
                print(self.escenarios[-1])
                choice = str(input("\n>>> "))
                setTimeout(0.5)
                os.system("cls")
                nombresReservados = [
                    "Nauj",
                    "Gigas",
                    "Bitspark",
                    "King",
                    "Python",
                    "Zero",
                    "Gatekeeper",
                    "Shao",
                    "Zoe",
                    "Shanon",
                    "Cor",
                    "Corgi"
                ]
                if choice in nombresReservados:
                    NR = DetectarNombrePascua(choice)
                    NR.concedirPascua()
                    anyKey2Continue()
                else:
                    print("Hmm... Entiendo.")
                    anyKey2Continue()
            print(self.escenarios[self.idx])
            anyKey2Continue()
            self.idx += 1
