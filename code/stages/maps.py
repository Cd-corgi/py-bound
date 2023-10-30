import os
import json
import code.functions as m
from code.clases import *
import main 

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
        while self.idx < len(self.escenarios):
            if self.idx == len(self.escenarios) - 1:
                print(self.escenarios[-1])
                choice = str(input("\n>>> "))
                m.setTimeout(0.5)
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
                    m.anyKey2Continue()
                    self.idx = 999
                    break
                else:
                    print("Hmm... Entiendo.")
                    m.anyKey2Continue()
            print(self.escenarios[self.idx])
            m.setTimeout(1.5)
            m.anyKey2Continue()
            self.idx += 1
        m.setTimeout(3.5)
        print("Entonces, si crees que soy lo que le temes... Rindete, o sufre las consecuencias.")
        m.anyKey2Continue()
        m.setTimeout(3.5)
        print("¡DESPIERTA YA!")
        m.anyKey2Continue()
        m.setTimeout(5.2)
        print("De la nada ese bosque se torna tan brillante como la ventana de una mañana soleada de un otoño. Te acabas de despertar.")
        m.anyKey2Continue()
        eve = DarEvento("introduccion")
        eve.registrarEventoTemporal(main.tempPath)
        

# segundo escenario

class EscenarioCasa:
    def __init__(self, playerData: object):
        self.playerData = playerData
        self.dialogo = [
            "",
            "",
            ""
        ]
    
    def EleccionRutas(self):
        pass
