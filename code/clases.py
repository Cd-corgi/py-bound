import os
import json
import code.functions as m
import main


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
        elif name == "Zoe".lower():
            print("La dulce cara para uno pero es peligrosa si se le da un arma. . .")
        elif name == "Shanon".lower():
            print("La encarnación de la maldad, es dulce. . .")
        elif name == "Cor".lower():
            print("¡NO MENCIONES ESA FACETA!")
        elif name == "Corgi".lower():
            print("Es un viejo conocido... No tan frecuete.")


class GuardarPartida:
    def __init__(self, tempDatos: object):
        self.tempDatos = tempDatos

    def compararDatos(self):
        consult = main.dd["player"]
        datosDeLaDb = {}
        datosDeTemp = {}
        datosdb = consult.find({"nombre": self.tempDatos["nombre"]})
        for i in datosdb:
            for x in i:
                if x != "_id":
                    datosDeLaDb[x] = i[x]
        for x in self.tempDatos:
            datosDeTemp[x] = self.tempDatos[x]
        if datosDeTemp == datosDeLaDb:
            os.system("cls")
            print("Guardando ...")
            m.setTimeout(3.0)
            try:
                for x in datosDeTemp:
                    consult.update_one({"nombre": datosDeTemp[x]}, {
                                       "$set": {x: datosDeTemp[x]}})
                os.system("cls")
                print("¡Partida Guardada!")
                m.anyKey2Continue()
            except Exception as e:
                raise print("Error en la DB: ", e)
        else:
            text = ""
            while text.lower() != "s" and text.lower() != "n" and len(text) == 0:
                print(
                    "Tienes datos existente en nuestro sistema...\n\n¿Desea sobreescribir el progreso?")
                text = str(input("\n>>> "))
                if text.lower() == "s":
                    os.system("cls")
                    print("Guardando ...")
                    for x in datosDeTemp:
                        consult.update_one({"nombre": datosDeTemp["nombre"]}, {
                                           "$set": {x: datosDeTemp[x]}})
                    m.setTimeout(3.0)
                    os.system("cls")
                    print("¡Datos Guardados!")
                    m.anyKey2Continue()
                elif text.lower() == "n":
                    text2 = ""
                    while text2.lower() != "s" and text2.lower() != "n":
                        os.system("cls")
                        print("¿Estás segur@? S/N")
                        text2 = str(input("\n>>> "))
                        if text2 == "S" or text2 == "s":
                            os.system("cls")
                            text = "n"
                        elif text2 == "N" or text2 == "n":
                            text = ""
                            os.system("cls")
                        else:
                            os.system("cls")
                            print("Elección no valida ...")
                            m.anyKey2Continue()
                else:
                    os.system("cls")
                    print("Elección no valida ...")
                    text = ""
                    m.anyKey2Continue()
