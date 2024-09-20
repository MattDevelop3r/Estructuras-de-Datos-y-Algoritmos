from listaCursor import lista

def mostrar_menu():
    print("\n--- Menú de opciones ---")
    print("1. Insertar elemento por posición")
    print("2. Insertar elemento por contenido")
    print("3. Suprimir elemento")
    print("4. Recuperar elemento")
    print("5. Buscar elemento")
    print("6. Obtener primer elemento")
    print("7. Obtener último elemento")
    print("8. Obtener siguiente posición")
    print("9. Obtener anterior posición")
    print("10. Recorrer lista")
    print("11. Obtener sucesor")
    print("12. Obtener predecesor")
    print("13. Verificar si está vacía")
    print("0. Salir")

def main():
    tamanio = int(input("Ingrese el tamaño máximo de la lista: "))
    mi_lista = lista(tamanio)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            elemento = int(input("Ingrese el elemento a insertar: "))
            posicion = int(input("Ingrese la posición de inserción: "))
            if mi_lista.insertarPorPosicion(elemento, posicion):
                print("Elemento insertado correctamente.")
            else:
                print("No se pudo insertar el elemento.")

        elif opcion == "2":
            elemento = int(input("Ingrese el elemento a insertar: "))
            if mi_lista.insertarPorContenido(elemento):
                print("Elemento insertado correctamente.")
            else:
                print("No se pudo insertar el elemento.")

        elif opcion == "3":
            posicion = int(input("Ingrese la posición del elemento a suprimir: "))
            if mi_lista.suprimir(posicion):
                print("Elemento suprimido correctamente.")
            else:
                print("No se pudo suprimir el elemento.")

        elif opcion == "4":
            posicion = int(input("Ingrese la posición del elemento a recuperar: "))
            elemento = mi_lista.recuperar(posicion)
            if elemento is not None:
                print(f"El elemento en la posición {posicion} es: {elemento}")

        elif opcion == "5":
            elemento = int(input("Ingrese el elemento a buscar: "))
            posicion = mi_lista.buscar(elemento)
            if posicion is not None:
                print(f"El elemento {elemento} está en la posición {posicion}")
            else:
                print("Elemento no encontrado.")

        elif opcion == "6":
            primer = mi_lista.primerElemento()
            if primer is not None:
                print(f"El primer elemento es: {primer}")

        elif opcion == "7":
            ultimo = mi_lista.ultimoElemento()
            if ultimo is not None:
                print(f"El último elemento es: {ultimo}")

        elif opcion == "8":
            posicion = int(input("Ingrese la posición actual: "))
            siguiente = mi_lista.siguientePosicion(posicion)
            if siguiente is not None:
                print(f"La siguiente posición es: {siguiente}")

        elif opcion == "9":
            posicion = int(input("Ingrese la posición actual: "))
            anterior = mi_lista.anteriorPosicion(posicion)
            if anterior is not None:
                print(f"La posición anterior es: {anterior}")

        elif opcion == "10":
            mi_lista.recorrer()

        elif opcion == "11":
            elemento = int(input("Ingrese el elemento para encontrar su sucesor: "))
            sucesor = mi_lista.sucesor(elemento)
            if sucesor is not None:
                print(f"El sucesor de {elemento} es: {sucesor}")
            else:
                print("No se encontró sucesor.")

        elif opcion == "12":
            elemento = int(input("Ingrese el elemento para encontrar su predecesor: "))
            predecesor = mi_lista.predecesor(elemento)
            if predecesor is not None:
                print(f"El predecesor de {elemento} es: {predecesor}")
            else:
                print("No se encontró predecesor.")

        elif opcion == "13":
            if mi_lista.vacia():
                print("La lista está vacía.")
            else:
                print("La lista no está vacía.")

        elif opcion == "0":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()