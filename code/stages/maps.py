import os
import json
import code.functions as m
from code.clases import *
import code.games.game as si
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
                    self.idx = 999
                    break
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
            "Estás en tu habitación... Ves a tu alrededor y notas que el dia está calido para iniciar tu rutina diaria.\n\nTomas tu {generoPalabra-ropaje}, Equipas tus ultimos libros del dia de escuela y bajas a la cocina...",
            "Bajas a la cocina y tu mamá {0}, te prepara el desayuno preguntandote.",
        ]
        self.eventos = [
            "Vas a la sala, un lugar algo espacioso... Hay puertas donde te llevan a varios lugares de la misma.\n¿A donde irás o harás?",
            "Te dirijes al patio. Supongo que quieres ir a visitar al granero... O saludar a un compañero",
            "Vuelves a tu habitación. No se por que volveras pero ahí vas",
            "Bajas al sotano. Revisas algunas cajas, te aburres y retornas a la sala.",
            "Retomas tu rumbo tomando tu morral y estás {generoPalabra-listo} para ir a la escuela.",
        ]
        self.elecciones = ["Explorar", "Hablar", "Inventario", "Opciones"]

    def EleccionRutas(self):
        ese = "casa"
        data = si.cargarTempDatos()
        ndata = m.loadNPCData(0)
        i = 0
        se = ""
        if data["genero"] == "niño":
            se = "male"
        else:
            se = "female"
        while i < len(self.dialogo):
            if i == 1:
                print(self.dialogo[i].replace('{0}', ndata["nombre"]))
                m.setTimeout(3.5)
                print("\n", m.RemplazarPalabras(
                    main.wordPath, ndata["dialogos"][2], se))
                m.anyKey2Continue()
                print(m.RemplazarPalabras(main.wordPath, ndata["dialogos"][3], se).replace(
                    '{player}', self.playerData["nombre"]))
                m.setTimeout(3.0)
                print("Sientes algo de comodidad al desayunar con tu mamá... La comida tiene ese toque especial que queras vivir su sabor cada vez que reposas...")
                m.setTimeout(3.0)
                os.system("cls")
                guardar = GuardarPartida(data, ese, None)
                guardar.compararDatos()
                i = 999
            else:
                print(m.RemplazarPalabras(main.wordPath, self.dialogo[i], se))
                m.setTimeout(2.5)
                m.anyKey2Continue()
                i += 1
        i = 0
        while self.eventos.index(self.eventos[i]) != 4:
            print(self.eventos[i])
            m.setTimeout(3.5)
            print("[1] Explorar\n[2] Hablar\n[3] Inventario\n[4] Opciones")
            elec = int(input("\n>>> "))
            if elec == 1:
                pass
            if elec == 2:
                os.system("cls")
                sis = ProcesarEleccion(ese, self.playerData, elec)
                sis.darElecciones()
            if elec == 3:
                if len(self.playerData["inventario"]) > 0:
                    sis = ProcesarEleccion(ese, self.playerData, elec)
                    sis.darElecciones()
                else:
                    os.system("cls")
                    print("Al parecer tu mochila anda vacia... Intenta obtener algo.")
                    m.anyKey2Continue()
            if elec == 4:
                sis = ProcesarEleccion(ese, self.playerData, elec)
                sis.darElecciones()
        else:
            m.anyKey2Continue()
            exit(0)
            pass

# tercer escenario