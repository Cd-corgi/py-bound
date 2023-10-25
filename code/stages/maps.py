import os
import json
from code.functions import *
from code.clases import *
from main import tempPath

# primer escenario


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
        anyKey2Continue()
        while self.idx < len(self.escenarios):
            if self.idx == len(self.escenarios) - 1:
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
                    self.idx = 999
                    break
                else:
                    print("Hmm... Entiendo.")
                    anyKey2Continue()
            print(self.escenarios[self.idx])
            setTimeout(1.5)
            anyKey2Continue()
            self.idx += 1
        setTimeout(3.5)
        print("Entonces, si crees que soy lo que le temes... Rindete, o sufre las consecuencias.")
        anyKey2Continue()
        setTimeout(3.5)
        print("¡DESPIERTA YA!")
        anyKey2Continue()
        setTimeout(5.2)
        print("De la nada ese bosque se torna tan brillante como la ventana de una mañana soleada de un otoño. Te acabas de despertar.")
        anyKey2Continue()
        eve = DarEvento("introduccion")
        eve.registrarEventoTemporal(tempPath)

# segundo escenario

class EscenarioCasa:
    def __init__(self, playerData: object):
        self.playerData = playerData
    
    def EleccionRutas(self):
        pass
