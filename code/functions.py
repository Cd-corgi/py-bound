import time
from colorama import *
import msvcrt as keyword
import os
import json
import keyboard as key


def setTimeout(ms: float):
    time.sleep(ms)


def anyKey2Continue():
    print("\n\nPulsa cualquier tecla para continuar ...")
    Key = keyword.getwch()
    os.system("cls")
    return


def DetectarSiHayPartida():
    rutaDePartida = './db/player.json'
    if os.path.isfile(rutaDePartida):
        return True
    else:
        return False


def modificarDatos(dato: str, content, path: str):
    try:
        with open(path, 'r') as f:
            data = json.load(f)

        data[dato] = content

        with open(path, 'w') as f:
            json.dump(data, f)
        pass
    except Exception as e:
        print("Un error ha ocurrido... ", e)
        os.system("exit()")
        pass


def registrarUsuario():
    i = 0

    dialogos = [
        "¿Comó te llamas?",
        "¿Eres niño o niña?",
        "¿Algo que te gusta?",
        "Elige tu color de dialogo (solo los numeros):\n1: Azul\n2: Verde\n3: Rojo\n4: Negro",
        "Y por ultimo elije tu sistema de combate:\n\n[A] Opción\n[B] Reto (Piedra, papel o tijeras)\n[C] Dejar que el sistema me elija una.",
        "Ok, ahora veamos si estos datos están bien."
    ]

    terminado = False

    with open('./code/templates/playerTemplate.json', 'r') as obb:
        data = json.load(obb)

    while terminado != True:
        datos = data
        Texto = ""
        while not Texto or len(Texto) == 0:
            print(dialogos[i])
            Texto = str(input("\n>>> "))
            if not Texto or len(Texto) == 0:
                print("No puedes tener un nombre muy corto...")
                keyword.getwch()
                os.system("cls")
            else:
                datos["nombre"] = Texto

        os.system("cls")
        i += 1

        Texto = ""
        while not Texto or len(Texto) == 0:
            print(dialogos[i])
            Texto = str(input("\n>>> "))
            if not Texto or len(Texto) == 0:
                print("Debes elegir un genero...")
                keyword.getwch()
                os.system("cls")
            else:
                datos["genero"] = Texto

        os.system("cls")
        i += 1

        Texto = ""
        while not Texto or len(Texto) == 0:
            print(dialogos[i])
            Texto = str(input("\n>>> "))
            if not Texto or len(Texto) == 0:
                Texto = "Amor"
                datos["gusto"] = Texto
                os.system("cls")
            else:
                datos["gusto"] = Texto

        os.system("cls")
        i += 1

        Texto = 0
        validarColor = [1, 2, 3, 4]
        valido = Texto in validarColor
        while valido is False:
            print(dialogos[i])
            Texto = int(input("\n>>> "))
            valido = Texto in validarColor
            if valido is True:
                datos["color"] = Texto
            else:
                print("Color no valido o no existente...")
                anyKey2Continue()
                os.system("cls")

        os.system("cls")
        i += 1
        Texto = 0
        inputChecker = ""
        while Texto != 1 and Texto != 2:
            print(dialogos[i])
            inputChecker = getInput()
            if inputChecker == 'a':
                Texto = 1
                datos["combate"] = Texto
                break
            elif inputChecker == 'b':
                Texto = 2
                datos["combate"] = Texto
                break
            elif inputChecker == 'c':
                Texto = 1
                datos["combate"] = Texto
                break
            else:
                os.system("cls")

        os.system("cls")
        i += 1
        Texto = ""
        while not Texto or len(Texto) == 0:
            print(dialogos[i])
            color = cargarColor(datos["color"])
            print(color + "\nNomre:\t", datos["nombre"], "\nGenero:\t", datos["genero"],
                  "\nGusto:\t", datos["gusto"], "\nColor:\t", datos["color"], "\nCombate:\t", datos["combate"])
            print("\n\n¿Así está bien? (S/N)")
            Texto = str(input("\n>>> "))
            if not Texto or len(Texto) == 0:
                print("Elige una opción valida ...")
                anyKey2Continue()
                os.system("cls")
            else:
                if Texto == 'S':
                    terminado = True
                    os.system("cls")
                    print("Creando partida... Espere un momento.")
                    setTimeout(5)
                    with open('./db/player.json', 'w') as d:
                        data = json.dump(datos, d)
                    os.system("cls")
                    print("¡Partida creada y guardada!")
                    with open('./code/temp/currentP.json', 'w') as pr:
                        data2 = json.dump(datos, pr)
                    anyKey2Continue()
                    os.system("cls")
                elif Texto == 'N':
                    terminado = False
                    i = 0
                    os.system("cls")
                    print("Entonces iniciemos de nuevo ...")
                    anyKey2Continue()
                    os.system("cls")

                else:
                    print("Elige una opción valida ...")
                    anyKey2Continue()
                    os.system("cls")
                    i = i
                    Texto = ""
    else:
        print("Bueno... Aqui inicia nuestra aventura.")
        anyKey2Continue()
        return


def cargarColor(color: int):
    if color == 1:
        bg = Back.BLUE + Fore.WHITE
    if color == 2:
        bg = Back.GREEN + Fore.BLACK
    if color == 3:
        bg = Back.RED + Fore.WHITE
    if color == 4:
        bg = Back.BLACK + Fore.WHITE
    return bg


def cargarDatos():
    with open('./db/player.json') as profile:
        data = json.load(profile)
    return data


def puntsus(duration: float):
    i = 0
    char = ". . ."
    for text in char:
        print(text, end="")
        time.sleep(duration)


def getInput():
    while True:
        if key.is_pressed('a'):
            input("################################################\n\n")
            return 'a'
        elif key.is_pressed('b'):
            input("################################################\n\n")
            return 'b'
        elif key.is_pressed('c'):
            input("################################################\n\n")
            return 'c'


def loadNPCDialog(char: str, charPos: int):
    with open('./code/templates/npcs.json') as character:
        data = json.load(character)
    return data[charPos]


def modificarTemp(dato: str, content, path: str, obj: str, newItems: list):
    with open(path) as file:
        data = json.open(file)

    if isinstance(data[dato], list) is True:
        # para lists de eventos nada mas.
        if dato == "inventario":
            if len(data[dato]) == 0:
                # añade los items por primera vez en caso de no tener ningun item
                for i in range(len(newItems)):
                    data[dato].append(newItems[i])
            else:
                lista_items_existentes = []
                i = 0
                for p in data[dato]:
                    for x in newItems:
                        if p['nombre'] == x['nombre']:
                            lista_items_existentes.append(x)
                print(lista_items_existentes)
                
    if isinstance(data[dato], object) is True:
        # para ingresar datos de un objeto
        data[dato][obj] = data[dato].get(obj) + content
    
# def main():
#     registrarUsuario()


# main()
