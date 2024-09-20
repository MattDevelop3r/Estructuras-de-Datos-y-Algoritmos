from classColaEncadenada import Cola
def menu():
    cola = Cola()
    
    while True:
        print("\n--- Menú de Opciones ---")
        print("1. Insertar elemento en la cola")
        print("2. Suprimir elemento de la cola")
        print("3. Recorrer cola")
        print("0. Salir")
        
        opcion = input("Elige una opción: ")

        if opcion == '1':
            elem = input("Ingresa el elemento a insertar: ")
            cola.insertar(elem)
            print(f"Elemento '{elem}' insertado.")
        
        elif opcion == '2':
            elem_suprimido = cola.suprimir()
            if elem_suprimido is not None:
                print(f"Elemento '{elem_suprimido}' suprimido.")

        elif opcion == '3':
            cola.recorrer()     
 
        elif opcion == '0':
            print("Saliendo...")
            break

        else:
            print("Opción no válida, intenta nuevamente.")

# Ejecutar el menú
menu()
