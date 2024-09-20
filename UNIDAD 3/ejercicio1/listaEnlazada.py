class Nodo():
    __dato: object
    __siguiente: object
    def __init__(self, dato=None):
        self.__dato = dato
        self.__siguiente = None

    def setDato(self, x):
        self.__dato = x
    
    def getDato(self):
        return self.__dato
    
    def setSiguiente(self, xp):
        self.__siguiente = xp
    
    def getSiguiente(self):
        return self.__siguiente

class ListaEnlazada:
    def __init__(self):
        self.__primero = None
        self.__ultimo = None
        self.__cantidad = 0

    def Vacio(self):
        return self.__primero is None

    def Insertar(self, L, posicion):
        nuevo_nodo = Nodo(L)
        if posicion == 0:  # Inserción en la primera posición
            nuevo_nodo.setSiguiente(self.__primero)
            self.__primero = nuevo_nodo
            if self.__cantidad == 0:
                self.__ultimo = nuevo_nodo
        else:
            if posicion > self.__cantidad or posicion < 0:
                print("La posición no es válida")
                return
            actual = self.__primero
            for i in range(posicion - 1):
                actual = actual.getSiguiente()
            nuevo_nodo.setSiguiente(actual.getSiguiente())
            actual.setSiguiente(nuevo_nodo)
            if nuevo_nodo.getSiguiente() is None:  # Si es el último nodo
                self.__ultimo = nuevo_nodo
        self.__cantidad += 1

    def Recorrer(self):
        if self.Vacio():
            print("La lista está vacía")
            return
        actual = self.__primero
        i = 0
        while actual is not None:
            print("El elemento {}, posición {}".format(actual.getDato(), i))
            actual = actual.getSiguiente()
            i += 1

    def Suprimir(self, posicion):
        if self.Vacio():
            print("La lista está vacía, no se puede eliminar ningún elemento")
            return
        if posicion < 0 or posicion >= self.__cantidad:
            print("Posición no válida")
            return
        if posicion == 0:  # Eliminar el primer nodo
            eliminado = self.__primero.getDato()
            self.__primero = self.__primero.getSiguiente()
            if self.__primero is None:
                self.__ultimo = None
        else:
            actual = self.__primero
            for i in range(posicion - 1):
                actual = actual.getSiguiente()
            eliminado = actual.getSiguiente().getDato()
            actual.setSiguiente(actual.getSiguiente().getSiguiente())
            if actual.getSiguiente() is None:  # Si eliminamos el último nodo
                self.__ultimo = actual
        self.__cantidad -= 1
        print("Se eliminó el elemento {}".format(eliminado))

    def Buscar(self, buscado):
        if self.Vacio():
            print("La lista está vacía")
            return
        actual = self.__primero
        i = 0
        while actual is not None:
            if actual.getDato() == buscado:
                print("El elemento {} está en la posición {}".format(buscado, i))
                return
            actual = actual.getSiguiente()
            i += 1
        print("El elemento {} no está en la lista".format(buscado))
    
    def Recuperar(self, posicion):
        if posicion < 0 or posicion >= self.__cantidad:
            return None
        
        actual = self.__primero
        for i in range(posicion):
            actual = actual.getSiguiente()
        
        return actual.getDato()

    def PrimerElemento(self):
        if not self.Vacio():
            return self.__primero.getDato()

    def UltimoElemento(self):
        if not self.Vacio():
            return self.__ultimo.getDato()

    def Siguiente(self, posicion):
        if posicion >= self.__cantidad - 1:
            print("No hay siguiente")
        else:
            actual = self.__primero
            for i in range(posicion):
                actual = actual.getSiguiente()
            print("El siguiente es: {}".format(actual.getSiguiente().getDato()))

    def Anterior(self, posicion):
        if posicion == 0:
            print("No hay anterior")
        else:
            actual = self.__primero
            for i in range(posicion - 1):
                actual = actual.getSiguiente()
            print("El anterior es: {}".format(actual.getDato()))