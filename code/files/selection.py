import os
import json
import msvcrt
import main

pp = main.tempPath


class CheckPlyName:
    def __init__(self, nPlayer: str, pPath: str):
        self.nPlayer = nPlayer

    def ConfirmName(self):
        with open(pp, 'r') as f:
            data = json.load(f)
        if self.nPlayer == "B.I.T.S" or self.nPlayer.lower() == "b.i.t.s":
            data["inventario"].append(
                {"nombre": "Caja con pantalla", "cantidad": 1})
            return data["inventario"]
        else:
            data["inventario"] = []
            return data["inventario"]
