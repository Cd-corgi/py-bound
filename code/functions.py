import time
from colorama import *
import msvcrt as keyword
import os
import json
import keyboard as key
from random import *
from db.schemas.player import Pschema
from main import dd
from code.files.selection import *


def setTimeout(ms: float):
    time.sleep(ms)


def anyKey2Continue():
    print("\n\nPulsa cualquier tecla para continuar ...")
    Key = keyword.getwch()
    os.system("cls")
    return


def DetectarSiHayPartida():
    coleccion = dd["player"]
    consulta = coleccion.find({})
    indexes = []
    for i in consulta:
        indexes.append(i)
    if len(indexes) > 0:
        return True
    else:
        return False
    # rutaDePartida = './db/player.json'
    # if os.path.isfile(rutaDePartida):
    #     return True
    # else:
    #     return False


def modificarDatos(dato: str, content):
    try:
        col = dd["player"]
        re = col.find({})
        for i in re:
            i[dato] = content
            up = col.update_one({"nombre": i["nombre"]}, {
                                "$set": {dato: content}})
            break
        return True
    except Exception as e:
        print("Un error ha ocurrido... ", e)
        exit(0)


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
                recoNombre = CheckPlyName(
                    datos["nombre"],  './code/templates/playerTemplate.json')
                yes = recoNombre.ConfirmName()
                if len(yes) > 0:
                    datos["inventario"].append(recoNombre.ConfirmName()[0])
                else:
                    datos["inventario"] = []
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
                    guardarPlayer(datos)
                    # with open('./db/player.json', 'w') as d:
                    #     data = json.dump(datos, d)
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
    collection = dd["player"]
    search = collection.find({})
    for i in search:
        data = i
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


def RemplazarPalabras(wordPath: str, string: str, playerG: str):
    with open(wordPath, 'r') as file:
        data = json.load(file)
    if playerG == 'female':
        for o in data["female"]:
            string = str(string.replace(o, data["female"][o]))
    else:
        for o in data["male"]:
            string = str(string.replace(o, data["male"][o]))
    return string


def randomRange(a, b):
    return round(uniform(a, b), 2)


def guardarPlayer(datos: object):
    col = dd["player"]
    schem = Pschema(datos)
    # print(schem)
    try:
        col.insert_one(schem)
    except Exception as e:
        print(e)


def loadNPCData(pos: int):
    with open('./code/templates/npcs.json') as f:
        data = json.load(f)
    return data[pos]

def frasesRandom():
    frases = [
        "¿Sabias que una cabra verde siempre está en la zona de juegos? Está usando su caos.",
        "¿Eres realmente cuerdo en exponer tu vida por una baya? Es tu caso mi estimado.",
        "FOTOSINTESIS",
        "Nunca confies en una cabra montesa... Son locas.",
        "Recuerda desinstalar Leage of Legends.",
        "Pro tip: Da 'enter' para ir interactuando.",
        "\"La baya magica es una mentira\"",
        "BLEEE~ \"DaKuNi\"",
        "Nintendo no sabe que tengo gradius en su codigo... Shh",
        "Para desbloquear el modo grafico, paga unos 5 dolares... Apoyame.",
        "朝日からその文化にインスピレーションを受けて…無理に伝承を残さないでください",
        "Eres un grandisimo puñetas...",
        "Sparkles estubo aqui... No se lo digas a Bitspark",
        "Silksong es real",
        "Earthbound es mi adicción.",
        "Aqui no hay Elles o Ellxs... Se lo que nacistes, no lo niegues carajo.",
        "MAKAROV"
    ]
    
    return frases[int(uniform(0, (len(frases) - 1)))]