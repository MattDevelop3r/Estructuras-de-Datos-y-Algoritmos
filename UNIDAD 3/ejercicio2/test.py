from listaSecuencialContenido import ListaSecuencial

def mostrar_menu():
    print("\n--- Menú de opciones ---")
    print("1. Insertar elemento")
    print("2. Suprimir elemento")
    print("3. Buscar elemento")
    print("4. Recorrer lista")
    print("5. Obtener primer elemento")
    print("6. Obtener último elemento")
    print("7. Obtener elemento siguiente")
    print("8. Obtener elemento anterior")
    print("9. Verificar si está vacío")
    print("10. Verificar si está lleno")
    print("0. Salir")

def main():
    tamanio = int(input("Ingrese el tamaño de la lista secuencial: "))
    lista = ListaSecuencial(tamanio)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            elemento = int(input("Ingrese el elemento a insertar: "))
            posicion = int(input("Ingrese la posición de inserción: "))
            lista.InsertarPorContenido(elemento, posicion)
        elif opcion == "2":
            posicion = int(input("Ingrese la posición del elemento a suprimir: "))
            lista.SuprimirPorContenido(posicion)
        elif opcion == "3":
            elemento = int(input("Ingrese el elemento a buscar: "))
            lista.Buscar(elemento)
        elif opcion == "4":
            lista.Recorrer()
        elif opcion == "5":
            primer = lista.PrimerElemento()
            if primer is not None:
                print(f"El primer elemento es: {primer}")
            else:
                print("La lista está vacía")
        elif opcion == "6":
            ultimo = lista.UltimoElemento()
            if ultimo is not None:
                print(f"El último elemento es: {ultimo}")
            else:
                print("La lista está vacía")
        elif opcion == "7":
            posicion = int(input("Ingrese la posición del elemento: "))
            lista.Siguiente(posicion)
        elif opcion == "8":
            posicion = int(input("Ingrese la posición del elemento: "))
            lista.Anterior(posicion)
        elif opcion == "9":
            if lista.Vacio():
                print("La lista está vacía")
            else:
                print("La lista no está vacía")
        elif opcion == "10":
            if lista.Lleno():
                print("La lista está llena")
            else:
                print("La lista no está llena")
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()