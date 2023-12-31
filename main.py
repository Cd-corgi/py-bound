##########################################################

import msvcrt
from colorama import *
import os
from code.functions import *
from code.clases import *
from code.games.game import mGame
from db.connection import *
import pymongo
from dotenv import *
init()


##### global variables #####

tempPath = './code/temp/currentP.json'
wordPath = './code/templates/genreWords.json'
load_dotenv()
databaseUrl = os.getenv('MONGO_CON')
client = establecerConexion(databaseUrl)
dd = client.test

########################################################


def main():
    global dd
    global wordPath
    global tempPath
    os.system("cls")
    print(Back.WHITE + Fore.BLUE + "Corgi presents...\n\n\n")
    print(Back.WHITE + """Para solo con el fin de programar sin tener que usar a mano propia el uso de Pygame. Cada vez que haga una update, meteré mas cositas.""")
    setTimeout(5)
    print("""\n\nUna pequeña aldea que donde un solo aldeano tiene un objetivo simple de conseguir unas bayas magicas que se encuentran en el otro lado de la aldea... ¡No se sabe si puede haber monstruos!""")
    setTimeout(5)
    os.system("cls")
    eleccion = 0
    while eleccion != 1 and eleccion != 2 and eleccion != 9:
        print("""PyBound - Version 0.0.5\nUna parodia de Earthbound pero con python en su codigo.""")
        setTimeout(3)
        continuar = DetectarSiHayPartida()
        dialogo = "\nElija una opción:\n\n1. Nueva Partida\n2. Cargar Partida\n9. Salir\n\n"
        print(dialogo)
        eleccion = input(">>> ")
        if eleccion == '' or not eleccion or eleccion is None:
            eleccion = 0
        eleccion = int(eleccion)
        if eleccion == 1:
            os.system("cls")
            print("Pero primero tendremos que saber... ¿Quíen eres?\n\n")
            if continuar == True:
                print(
                    "\n\nTienes una partida existente en la app. Tus datos anteriores fueron borrados\n\n")
                borrarDato = dd["player"].find({})
                for enc in borrarDato:
                    dd["player"].delete_one(enc)
            anyKey2Continue()
            registrarUsuario()
            mGame()
            eleccion = 0
        elif eleccion == 2:
            if continuar == True:
                os.system("cls")
                print("Espere....")
                setTimeout(3)
                elegir = 0
                while elegir != 1 and elegir != 2 and elegir != 3 and elegir != 9:
                    os.system("cls")
                    partidaCargada = cargarDatos()
                    custom = cargarColor(partidaCargada["color"])
                    print(custom + "Datos de la partida guardada:", "\n#########################################################", "\nNombre: ",
                          partidaCargada["nombre"], "\nGenero: ", partidaCargada["genero"], "\nNivel: ", partidaCargada["estadistica"].get("nivel"))
                    print(
                        """\n\n[1] Cargar | [2] Borrar | [3] Cambiar Colores | [9] Atras\n"""
                    )
                    elegir = int(input(">>> "))
                    if elegir == 1:
                        os.system("cls")
                        print("Cargando Progreso...")
                        rr = frasesRandom()
                        print(f"\n {rr}")
                        setTimeout(3.5)
                        part = CargarPartida(partidaCargada, tempPath)
                        os.system("cls")
                        print("Partida Cargada!")
                        anyKey2Continue()
                        part.ponerSuEvento()
                    elif elegir == 2:
                        os.system("cls")
                        col = dd["player"]
                        print("Tu partida fue borrada...")
                        anyKey2Continue()
                        eleccion = 0
                        col.delete_one({ "nombre": partidaCargada["nombre"] })
                    elif elegir == 3:
                        eleColor = 9
                        while eleColor != 1 and eleColor != 2 and eleColor != 3 and eleColor != 4 and eleColor != 0:
                            os.system("cls")
                            print(
                                "Elija una opción para cambiar el color:\n\n[1] Azul\n[2] Verde\n[3] Rojo\n[4] Negro\n[0] Cancelar\n")
                            eleColor = int(input(">>> "))
                            if eleColor == 1:
                                os.system("cls")
                                print("Cambiando el color...")
                                modificarDatos("color", eleColor)
                                setTimeout(3)
                                os.system("cls")
                                print(
                                    "Colores cambiados y guardados en la partida... Vuelva a cargar el progreso.")
                                anyKey2Continue()
                                eleccion = 0
                            elif eleColor == 2:
                                os.system("cls")
                                print("Cambiando el color...")
                                modificarDatos("color", eleColor)
                                setTimeout(3)
                                os.system("cls")
                                print(
                                    "Colores cambiados y guardados en la partida... Vuelva a cargar el progreso.")
                                anyKey2Continue()
                                eleccion = 0
                            elif eleColor == 3:
                                os.system("cls")
                                print("Cambiando el color...")
                                modificarDatos("color", eleColor)
                                setTimeout(3)
                                os.system("cls")
                                print(
                                    "Colores cambiados y guardados en la partida... Vuelva a cargar el progreso.")
                                anyKey2Continue()
                                eleccion = 0
                            elif eleColor == 4:
                                os.system("cls")
                                print("Cambiando el color...")
                                modificarDatos("color", eleColor)
                                setTimeout(3)
                                os.system("cls")
                                print(
                                    "Colores cambiados y guardados en la partida... Vuelva a cargar el progreso.")
                                anyKey2Continue()
                                eleccion = 0
                            elif eleColor == 0:
                                os.system("cls")
                                eleccion = 0
                            else:
                                print("")
                                os.system("cls")
                    elif elegir == 9:
                        os.system("cls")
                        eleccion = 0
                        break
                    elif not elegir or len(elegir) == 0:
                        print("Elección no valida... Reintente.")
                        anyKey2Continue()
                    else:
                        print("Elección no valida... Reintente.")
                        anyKey2Continue()
            else:
                os.system("cls")
                print(
                    "No tienes una partida existente... Deberás crear una partida nueva.")
                msvcrt.getwch()
                eleccion = 0
                os.system("cls")
        elif eleccion == 9:
            os.system("cls")
            os.system("exit()")
        else:
            os.system("cls")


if __name__ == '__main__':
    main()

########################################################
