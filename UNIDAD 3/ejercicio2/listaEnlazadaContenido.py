class Nodo:
    def __init__(self, dato=None):
        self.__dato = dato
        self.__siguiente = None

    def getDato(self):
        return self.__dato
    
    def setDato(self, dato):
        self.__dato = dato

    def getSiguiente(self):
        return self.__siguiente
    
    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente

class ListaEnlazadaPorContenido:
    def __init__(self):
        self.__primero = None
        self.__cantidad = 0

    def Vacio(self):
        return self.__primero is None

    def InsertarPorContenido(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.Vacio():
            self.__primero = nuevo_nodo
            print(f"El elemento insertado fue {dato}")
        else:
            actual = self.__primero
            anterior = None
            while actual is not None and actual.getDato() < dato:
                anterior = actual
                actual = actual.getSiguiente()
            if anterior is None:  # Insertar al inicio
                nuevo_nodo.setSiguiente(self.__primero)
                self.__primero = nuevo_nodo
            else:  # Insertar en medio o al final
                anterior.setSiguiente(nuevo_nodo)
                nuevo_nodo.setSiguiente(actual)
            print(f"El elemento insertado fue {dato}")
        self.__cantidad += 1

    def Recorrer(self):
        if self.Vacio():
            print("La lista está vacía, no se muestra ningún elemento")
        else:
            actual = self.__primero
            i = 0
            while actual is not None:
                print(f"El elemento {actual.getDato()}, posición {i}")
                actual = actual.getSiguiente()
                i += 1

    def SuprimirPorContenido(self, dato):
        if self.Vacio():
            print("La lista está vacía, no se puede eliminar ningún elemento")
            return
        actual = self.__primero
        anterior = None
        while actual is not None and actual.getDato() != dato:
            anterior = actual
            actual = actual.getSiguiente()
        if actual is None:
            print(f"El elemento {dato} no está en la lista")
        else:
            if anterior is None:  # Eliminar el primer nodo
                self.__primero = actual.getSiguiente()
            else:  # Eliminar un nodo en medio o al final
                anterior.setSiguiente(actual.getSiguiente())
            print(f"Se eliminó el elemento {dato}")
            self.__cantidad -= 1

    def Buscar(self, buscado):
        if self.Vacio():
            print("La lista está vacía")
            return
        actual = self.__primero
        i = 0
        while actual is not None:
            if actual.getDato() == buscado:
                print(f"El elemento {buscado} está en la posición {i}")
                return
            actual = actual.getSiguiente()
            i += 1
        print(f"El elemento {buscado} no está en la lista")

    def PrimerElemento(self):
        if not self.Vacio():
            return self.__primero.getDato()

    def UltimoElemento(self):
        if not self.Vacio():
            actual = self.__primero
            while actual.getSiguiente() is not None:
                actual = actual.getSiguiente()
            return actual.getDato()

    def Siguiente(self, posicion):
        if self.Vacio():
            print("La lista está vacía")
            return
        actual = self.__primero
        for i in range(posicion):
            if actual is not None:
                actual = actual.getSiguiente()
        if actual is not None and actual.getSiguiente() is not None:
            print(f"El siguiente es: {actual.getSiguiente().getDato()}")
        else:
            print("No hay siguiente")

    def Anterior(self, posicion):
        if self.Vacio():
            print("La lista está vacía")
            return
        if posicion == 0:
            print("No hay anterior")
            return
        actual = self.__primero
        for i in range(posicion - 1):
            if actual is not None:
                actual = actual.getSiguiente()
        if actual is not None:
            print(f"El anterior es: {actual.getDato()}")
