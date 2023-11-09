import os
import json
import code.functions as m
import main
import pandas
from code.files.selection import EasterEgg


class ItemsDeInventario:
    def __init__(self, nombre: str, cantidad: int):
        # Declaro los items a dar en clase...
        self.nombre = nombre
        self.cantidad = cantidad

    def darItem(self, path: str, objeto: str):
        # Abre el JSON temporal para modificar...
        with open(path, 'r') as f:
            data = json.load(f)
        # Crea una list para meter todos los nombres de los items
        getItems = []
        for checkItem in data[objeto]:
            # Aqui añade todos los nombres de los items a getItems
            getItems.append(checkItem["nombre"])
        # Si el nombre del item está en la list metido en la clase... Aumenta la cantidad del item a dar...
        if self.nombre in getItems:
            for aumentarItem in data[objeto]:
                if self.nombre == aumentarItem["nombre"]:
                    # Aumenta el numero de items...
                    aumentarItem["cantidad"] += self.cantidad
                    print("Da una cantidad de items", self.cantidad)
                    # Anuncia el dado de items y guarda los cambios en la temporal...
                    with open(path, 'w') as fi:
                        data = json.dump(data, fi)
        # En tal caso que no lo esté, lo añade al inventario...
        else:
            # Añade al inventario...
            data[objeto].append(
                {"nombre": self.nombre, "cantidad": self.cantidad})
            print("Te da el item: ", self.nombre)
            # Anuncia el añadido del item y lo guarda en la temporal...
            with open(path, 'w') as fi:
                data = json.dump(data, fi)

    def usarItem(self, path: str, objeto: str):
        with open(path, 'r') as f:
            data = json.load(f)
        for tenerItem in data[objeto]:
            if self.nombre == tenerItem["nombre"]:
                if tenerItem["cantidad"] >= 1:
                    tenerItem["cantidad"] -= self.cantidad
                    if tenerItem["cantidad"] < 1:
                        data[objeto].remove(tenerItem)
                else:
                    tenerItem["cantidad"] = 0
                    data[objeto].remove(tenerItem)
                print("Usas ", self.nombre, ". . .")
                m.setTimeout(1.5)
                os.system("cls")
                m.usoDelItem(self.nombre, self.cantidad)
                with open(path, 'w') as f:
                    j = json.dump(data, f)
                break

    def tirarItem(self, path: str, objeto: str):
        with open(path, 'r') as f:
            data = json.load(f)
        for getItem in data[objeto]:
            if self.nombre == getItem["nombre"]:
                if getItem["cantidad"] >= 1:
                    getItem["cantidad"] -= self.cantidad
                    if getItem["cantidad"] < 1:
                        data[objeto].remove(getItem)
                else:
                    getItem["cantidad"] = 0
                    data[objeto].remove(getItem)
                print("Has tirado x", self.cantidad,
                      " de ", self.nombre, ". . .")
                with open(path, 'w') as f:
                    j = json.dump(data, f)
                break


class DarEvento:
    def __init__(self, evento: str):
        self.evento = evento

    def registrarEventoTemporal(self, path: str):
        # Leyendo su archivo temporal.
        with open(path, 'r') as f:
            data = json.load(f)

        # Leyendo el archivo de eventos
        with open('./code/templates/events.json', 'r') as ev:
            evnt = json.load(ev)

        # Creando un while para en cuando ya tenga un trigger que está false
        obtenido = False
        i = 0
        while obtenido == False:
            if self.evento == evnt[i]:
                # Añade el evento al archivo temporal.
                data["listaDeEventos"].append(evnt[i])
                # Guarda los cambios en el temporal..
                with open(path, 'w') as f:
                    d = json.dump(data, f)
                # Cambia el trigger para dar fin al while
                obtenido = True
            else:
                i += 1
        pass


class DetectarNombrePascua:
    def __init__(self, nombre: str):
        self.nombre = nombre

    def concedirPascua(self):
        name = self.nombre.lower()
        if name == "Nauj".lower():
            print("Sin duda alguna es alguien temible. . .")
        elif name == "Gigas".lower():
            print("La personificación del odio. . . Entendible.")
        elif name == "Bitspark".lower():
            print("¡EL CAOS REPRESENTADA POR UNA CABRA!")
        elif name == "King".lower():
            print("¿Acaso te asusta un fan de pokémon?")
        elif name == "Python".lower():
            print("Eres parte de mi codigo. . .")
        elif name == "Zero".lower():
            print("Ese nombre no lo menciones aqui. . .")
        elif name == "Gatekeeper".lower():
            print("Este protocolo jamás fue dado para el creador. . .")
        elif name == "Shao".lower():
            print("No metas a Liu Kang en esto. . .")
        elif name == "Cor".lower():
            print("¡NO MENCIONES ESA FACETA!")
        elif name == "Corgi".lower():
            print("Es un viejo conocido... No tan frecuete.")


class GuardarPartida:
    def __init__(self, tempDatos: object):
        self.tempDatos = tempDatos

    def compararDatos(self):
        # Declaramos desde main y llamamos su collecion "player"
        consult = main.dd["player"]
        # Variables de objects para comparar (Vaya a linea 165)
        datosDeLaDb = {}
        datosDeTemp = {}
        # Hacemos una consulta general a mongoDB para que nos de un cursor de todos los datos de la coleccion player
        datosdb = consult.find({"nombre": self.tempDatos["nombre"]})
        # En caso de haber encontrado un dato, busca y itera por cada objeto
        for i in datosdb:
            # Por cada objeto encontrado, iterará por sus atributos
            for x in i:
                # Metemos a las variables excepto el atributo "_id"
                if x != "_id":
                    datosDeLaDb[x] = i[x]
        # Iteramos los datos temporales y lo añadimos a su objeto para comparar
        for x in self.tempDatos:
            datosDeTemp[x] = self.tempDatos[x]
        # Compara si el objeto temporal y el objeto de la db si tienen los mismos datos.
        if datosDeTemp == datosDeLaDb:
            # En caso de que sea True, guarda directamente. . .
            os.system("cls")
            print("Guardando ...")
            m.setTimeout(3.0)
            try:
                # recorre desde un FOR para actualizar cada atributo del documento
                for x in datosDeTemp:
                    consult.update_one({"nombre": datosDeTemp[x]}, {
                                       "$set": {x: datosDeTemp[x]}})
                # Listo, aqui termina en caso de que sean iguales los datos a guardar
                os.system("cls")
                print("¡Partida Guardada!")
                m.anyKey2Continue()
            except Exception as e:
                # Tira una excepcion en caso de que haya un error.
                raise print("Error en la DB: ", e)
        else:
            # Entra aqui en caso de que no sean iguales los datos temporales con la DB
            text = ""
            # While para recorrer en caso que no quiera sobreescribir y elije ninguna de las 2 opciones.
            while text.lower() != "s" and text.lower() != "n" and len(text) == 0:
                # Advierte el usuario al querer sobreescribir.
                print(
                    "Tienes datos existente en nuestro sistema...\n\n¿Desea sobreescribir el progreso?")
                text = str(input("\n>>> "))
                # Condicionamos la elección.
                if text.lower() == "s":
                    os.system("cls")
                    print("Guardando ...")
                    # Iteramos el dato temporal para actualizar los datos de la db
                    for x in datosDeTemp:
                        consult.update_one({"nombre": datosDeTemp["nombre"]}, {
                                           "$set": {x: datosDeTemp[x]}})
                    # Termina la sobreescritura de los datos...
                    m.setTimeout(3.0)
                    os.system("cls")
                    print("¡Datos Guardados!")
                    m.anyKey2Continue()
                elif text.lower() == "n":
                    # En caso de no querer sobreescribir. Te advierte que quieres continuar sin guardar.
                    text2 = ""
                    # Un while aislado para dejar a conocer si quiere o no continuar.
                    while text2.lower() != "s" and text2.lower() != "n":
                        os.system("cls")
                        print("¿Estás segur@? S/N")
                        text2 = str(input("\n>>> "))
                        # Si dice que si, termina aqui y continua.
                        if text2 == "S" or text2 == "s":
                            os.system("cls")
                            text = "n"
                        # En caso de negarse, vuelve a preguntar para sobreescribir la partida.
                        elif text2 == "N" or text2 == "n":
                            text = ""
                            os.system("cls")
                        # Su opcion invalida hace repetir esta desicion
                        else:
                            os.system("cls")
                            print("Elección no valida ...")
                            m.anyKey2Continue()
                # Si no elige un Si o un No, repite el aviso a sobreescribir.
                else:
                    os.system("cls")
                    print("Elección no valida ...")
                    text = ""
                    m.anyKey2Continue()

class ProcesarEleccion:
    def __init__(self, ese: str, dataPlayer: object, choice: int):
        self.dataPlayer = dataPlayer
        self.ese = ese
        self.choice = choice
    def darElecciones(self):
        if self.ese == "casa":
            if self.choice == 1:
                pass
            if self.choice == 2:
                os.system("cls")
                ply = self.dataPlayer["nombre"]
                print(f"¿Quieres decir algo, {ply}?")
                decir = str(input("\n>>> "))
                if len(decir) == 0 or not decir:
                    os.system("cls")
                    print("Entonces prefieres ahorrarlo para déspues...")
                    m.anyKey2Continue()
                    return
                elif decir == "start" and self.dataPlayer["nombre"] == "b.i.t.s":
                    print("Decides usar tu \"Caja con pantalla\" para intentar entretenerte un rato...\nLa Caja con pantalla empieza a mostrar contenido...")
                    m.setTimeout(3.5)
                    ae = EasterEgg(self.dataPlayer)
                    ae.ExecuteGame()
                else:
                    print(f"Acabas de decir \"{decir}\"... Nadie nota tu opinión...")
                    m.anyKey2Continue()
            if self.choice == 3:
                datos = {
                    'Item': [],
                    'Cantidad': []
                }
                for items in self.dataPlayer["inventario"]:
                    datos["Item"].append(items["nombre"])
                    datos["Cantidad"].append(items["cantidad"])
                os.system("cls")
                df = pandas.DataFrame(datos)
                pandas.set_option('display.max_columns', None)
                pandas.set_option("colheader_justify", "left")
                print(f"Inventario de {ply}")
                print("===========================================")
                print(df)
                m.anyKey2Continue()
                return