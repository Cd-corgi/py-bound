import os
import json
import msvcrt
import zipfile
import shutil
import dotenv
from pathlib import Path
from code.clases import *
dotenv.load_dotenv()
pp = os.getenv("TEMP_PATH")


class CheckPlyName:
    def __init__(self, nPlayer: str, pPath: str):
        self.nPlayer = nPlayer
        self.pPath = pPath
    def ConfirmName(self):
        with open(self.pPath, 'r') as f:
            data = json.load(f)
        if self.nPlayer == "B.I.T.S" or self.nPlayer.lower() == "b.i.t.s":
            data["inventario"].append(
                {"nombre": "Caja con pantalla", "cantidad": 1})
            return data["inventario"]
        else:
            data["inventario"] = []
            return data["inventario"]


class EasterEgg:
    def __init__(self, dataPlayer: object):
        self.dataPlayer = dataPlayer

    def ExecuteGame(self):
        PathE = os.getenv("CRYPTDIR")
        PathT = os.getenv("CRYPTTG")
        Destiny = os.getenv("ZIP_DESTINY")
        EAGA = os.getenv("EASTER_GAME_CRP")
        EAGAT = os.getenv("EASTER_GAME")
        game = os.getenv("GAME")
        delP = os.getenv("DELETION_DESTINY")

        self.Procc(PathT, PathE, Destiny, EAGA, EAGAT, game, delP)

    def Procc(self, archivoO, archivoD, DPath, gameC, gameD, ROM, DelPath):
        # Decrypt the App
        os.rename(archivoO, archivoD)
        # Extract the files
        with zipfile.ZipFile(archivoD, 'r') as Z:
            Z.extractall(DPath)
        # Encrypt the App
        os.rename(archivoD, archivoO)
        # Decrypt the game and execute it
        os.rename(gameC, gameD)
        os.system(
            "start code/files/emu/NES/virtuaNES.exe code/files/emu/Gr4D1u5.zip")
        # Check the App process is running ...
        process = 'VirtuaNES.exe'
        yes = self.checkProcess(process)
        while yes == True:
            yes = self.checkProcess(process)
        else:
            os.rename(gameD, gameC)
            p = Path(DelPath)
            shutil.rmtree(p)
            os.system("cls")
            print("Apagas tu Caja con pantalla... Te divertistes un ratito, pero debes seguir con tu dia.")
            m.anyKey2Continue()
            return
    def checkProcess(self, app: str):
        outP = os.popen('tasklist').read()
        if app in outP:
            return True
        else:
            return False
