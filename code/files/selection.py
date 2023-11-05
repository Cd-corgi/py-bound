import os
import json
import msvcrt
import main

pp = main.tempPath


class CheckPlyName:
    def __init__(self, nPlayer: str):
        self.nPlayer = nPlayer

    def ConfirmName(self):
        if self.nPlayer == "B.I.T.S" or self.nPlayer.lower() == "b.i.t.s":
            with open(pp, 'r') as f:
                data = json.load(f)
            data["inventario"].append(
                {"nombre": "Caja con pantalla", "cantidad": 1})
            with open(pp, 'w') as f:
                data = json.dump(f)
