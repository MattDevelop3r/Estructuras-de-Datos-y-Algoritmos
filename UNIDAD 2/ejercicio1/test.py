from classPilaSecuencial import Pila

def menu():
    pila = Pila()
    
    while True:
        print("\n--- Menú de Opciones ---")
        print("1. Insertar elemento en la pila")
        print("2. Suprimir elemento de la pila")
        print("3. Verificar si la pila está vacía")
        print("4. Recorrer la pila")
        print("0. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            elemento = input("Ingresa el elemento a insertar: ")
            pila.insertar(elemento)
        
        elif opcion == "2":
            elem = pila.suprimir()
            if elem != None:
                print(f"Elemento '{elem}' suprimido")
          
        elif opcion == "3":
            if pila.vacia():
                print("La pila está vacía.")
            else:
                print("La pila no está vacía.")
        
        elif opcion == "4":
            pila.recorrer()
        
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida, por favor selecciona una opción correcta.")

if __name__ == '__main__':
    menu()
