def use_the_force(mochila, elemento):
    if not mochila:
        return None
    elif mochila[0] == elemento:
        return 1
    else:
        objetos_sacados = use_the_force(mochila[1:], elemento)
        if not objetos_sacados:
            return None
        else:
            return objetos_sacados + 1


mochila = ["sable de luz", "comida", "capa", "brujula", "llaves", "sable de luz"]
elemento = input('Ingrese el elemento a buscar: ')


objetos_sacados = use_the_force(mochila, elemento)

if objetos_sacados == None:
    print(f"No se encontró {elemento} en la mochila")
else:
    print(f"Se encontró {elemento} después de sacar {objetos_sacados} objetos")
