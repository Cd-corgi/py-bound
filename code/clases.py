import os
import json

class ItemsDeInventario:
    def __init__(self, nombre: str, cantidad: int):
        self.nombre = nombre
        self.cantidad = cantidad

    def darItem(self, path: str, objeto: str):
        with open(path, 'r') as f:
            data = json.load(f)
        getItems = []
        for checkItem in data[objeto]:
            getItems.append(checkItem["nombre"])
        if self.nombre in getItems:
            for aumentarItem in data[objeto]:
                if self.nombre == aumentarItem["nombre"]:
                    aumentarItem["cantidad"] += self.cantidad
                    print("Da una cantidad de items", self.cantidad)
                    with open(path, 'w') as fi:
                        data = json.dump(data, fi)
        else:
            data[objeto].append(
                {"nombre": self.nombre, "cantidad": self.cantidad})
            print("Te da el item: ", self.nombre)
            with open(path, 'w') as fi:
                data = json.dump(data, fi)

    def usarItem(self, item: str, cantidad: int, path: str, objeto: str):
        pass
    
    def tirarItem(self, item: str, cantidad: int, path: str, objeto: str):
        pass