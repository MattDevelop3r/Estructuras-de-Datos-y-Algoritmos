from classPila import Pila

def muestraTorres(pila1, pila2, pila3, cant):
    aux1, aux2, aux3 = [], [], []

    # Guardar el estado de las pilas en las listas auxiliares
    while not pila1.vacia():
        aux1.append(pila1.suprimir())
    while not pila2.vacia():
        aux2.append(pila2.suprimir())
    while not pila3.vacia():
        aux3.append(pila3.suprimir())

    # Restaurar las pilas después de sacar los elementos
    for elem in reversed(aux1):
        pila1.insertar(elem)
    for elem in reversed(aux2):
        pila2.insertar(elem)
    for elem in reversed(aux3):
        pila3.insertar(elem)

    # Imprimir las torres de abajo hacia arriba
    for i in range(cant):
        elem1 = aux1[i] if i < len(aux1) else 0
        elem2 = aux2[i] if i < len(aux2) else 0
        elem3 = aux3[i] if i < len(aux3) else 0
        print(f"{elem1} --- {elem2} --- {elem3}")

def moverDisco(origen, destino):
    discoOrigen = origen.suprimir()

    if discoOrigen is None:
        print("No se puede mover un disco de una torre vacía.")
        return False

    if destino.vacia():
        destino.insertar(discoOrigen)
        return True

    discoDestino = destino.suprimir()
    destino.insertar(discoDestino)  # Volver a poner el disco en la torre destino

    if discoOrigen > discoDestino:
        print("No se puede mover un disco grande sobre uno más pequeño.")
        origen.insertar(discoOrigen)  # Volver a poner el disco en la torre origen
        return False

    destino.insertar(discoOrigen)
    return True

def torreshanoi():
    cantF = int(input("Ingrese la cantidad de fichas: "))
    torre1 = Pila(cantF)
    torre2 = Pila(cantF)
    torre3 = Pila(cantF)

    for i in range(cantF, 0, -1):
        torre1.insertar(i)

    while not torre3.llena():
        print("\nEstado actual:")
        muestraTorres(torre1, torre2, torre3, cantF)

        origen = int(input("Selecciona la torre de origen (1, 2, 3): "))
        destino = int(input("Selecciona la torre de destino (1, 2, 3): "))

        if origen == 1:
            torre_origen = torre1
        elif origen == 2:
            torre_origen = torre2
        elif origen == 3:
            torre_origen = torre3

        if destino == 1:
            torre_destino = torre1
        elif destino == 2:
            torre_destino = torre2
        elif destino == 3:
            torre_destino = torre3

        moverDisco(torre_origen, torre_destino)

    print("\n¡Felicitaciones! Has completado el juego.")
    muestraTorres(torre1, torre2, torre3, cantF)

if __name__ == "__main__":
    torreshanoi()