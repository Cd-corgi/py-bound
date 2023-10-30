def Pschema(data: object):
    PlayerSchema = {
        "nombre": data["nombre"],
        "genero": data["genero"],
        "gusto": data["gusto"],
        "color": data["color"],
        "combate": data["combate"],
        "inventario": [],
        "estadistica": {
            "xp": 0,
            "limiteXP": 50,
            "nivel": 1,
            "ataque": 5,
            "defensa": 5,
            "vida": 25,
        },
        "lugarDeGuardado": {
            "lugar": "",
            "zona": "",
        },
        "listaDeEventos": []
    }
    
    return PlayerSchema