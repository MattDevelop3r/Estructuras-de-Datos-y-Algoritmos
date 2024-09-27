from arbolBinario import ArbolBinarioBusqueda

def contarTotalNodos(subarbol):
    if subarbol is None:
        return 0
    else:
        return 1 + contarTotalNodos(subarbol.getIzquierda()) + contarTotalNodos(subarbol.getDerecha())

def verAltura(subarbol):
    if subarbol is None:
        return 0  # Un árbol vacío tiene altura 0
    
    # Calcular la altura de los subárboles izquierdo y derecho
    altura_izquierda = verAltura(subarbol.getIzquierda())
    altura_derecha = verAltura(subarbol.getDerecha())
    
    # La altura del árbol es el máximo de ambas alturas más 1 (por la raíz)
    return max(altura_izquierda, altura_derecha) + 1

    
if __name__ == '__main__':
    arbol = ArbolBinarioBusqueda()

    arbol.insertar(arbol.getRaiz(),20)
    arbol.insertar(arbol.getRaiz(),10)
    arbol.insertar(arbol.getRaiz(),30)
    arbol.insertar(arbol.getRaiz(),5)
    arbol.insertar(arbol.getRaiz(),60)
    arbol.insertar(arbol.getRaiz(),2)
    
    op = 1
    while op != 0:
        print('1_ Mostrar el nodo padre y el nodo hermano de un nodo ingresado')
        print('2_ Mostrar la cantidad de nodos del arbol')
        print('3_ Mostrar la altura del arbol')
        print('4_ Mostrar los sucesores de un nodo ingresado')
        print('5_ Salir del programa')


        op = int(input('Ingrese una opcion: '))

        if op == 1: 
            clave = int(input('Ingrese un número: '))
            nodo = arbol.buscar(arbol.getRaiz(), clave)
            if nodo is not None:
                print(f"El nodo con clave {clave} pertenece al árbol.")
                padre = arbol.getPadre(clave)
                if padre is None:
                    print("El nodo es la raíz, no tiene padre ni hermano.")
                else:
                    if clave > padre.getDato():
                        hermano = padre.getIzquierda()
                    else:
                        hermano = padre.getDerecha()
                    if hermano is not None:
                        print(f"El hermano del nodo con clave {clave} es: {hermano.getDato()}")
                    else:
                        print(f"El nodo con clave {clave} no tiene hermano.")
            else:
                print(f"El nodo con clave {clave} NO pertenece al árbol.")
            print()       
        elif op == 2:
            total_nodos = contarTotalNodos(arbol.getRaiz())
            print(f"El total de nodos en el árbol es: {total_nodos}")
        elif op == 3:
            print(f'La altura del arbol es: {verAltura(arbol.getRaiz())}')
        elif op == 4: 
            clave = int(input('Ingrese un nodo: ')) 
            nodo = arbol.buscar(arbol.getRaiz(), clave)
            if nodo is not None:
                if nodo.getDerecha() is None and nodo.getIzquierda() is None:
                    print('El elemento no tiene sucesores')
                else: 
                    print(f'Los sucesores del nodo con clave {clave}')
                    if nodo.getIzquierda() is not None:
                        arbol.InOrder(nodo.getIzquierda())
                    if nodo.getDerecha() is not None:
                        arbol.InOrder(nodo.getDerecha())
            else: 
                print(f"El nodo con clave {clave} NO pertenece al árbol.")
        else: print('Opcion incorrecta, ingrese nuevamente!')
    
    print("Saliendo del programa...")
    