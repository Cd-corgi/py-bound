import os
import json
from code.functions import *


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
                setTimeout(1.5)
                os.system("cls")
                usoDelItem(self.nombre, self.cantidad)
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

# Añadiendo mas clases en breve


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
