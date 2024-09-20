class Nodo:
    __dato: int
    __siguiente: object

    def __init__(self, dato):
        self.__dato = dato
        self.__siguiente = None
    
    def setDato(self, dato):
        self.__dato = dato
        
    def getDato(self):
        return self.__dato
    
    def setSiguiente(self, siguiente):
        self.__siguiente=siguiente

    def getSiguiente(self):
        return self.__siguiente   

class Pila:
    __tope: int
    __cant: int

    def __init__(self):
        self.__tope = None
        self.__cant = 0

    def vacia(self):
        return self.__tope is None
    
    def insertar(self, elem):
        nuevo_nodo = Nodo(elem)
        nuevo_nodo.setSiguiente(self.__tope)
        self.__tope = nuevo_nodo
        self.__cant += 1
        return elem
    
    def suprimir(self):
        if self.vacia():
            print("La pila está vacía, no se puede eliminar")
            return None
        else:
            elem = self.__tope.getDato()
            self.__tope = self.__tope.getSiguiente()
            self.__cant -= 1
            return elem
    
    def recorrer(self):
        if self.vacia():
            print("No se puede recorrer, pila vacía")
            return None
        else:
            actual = self.__tope
            while actual is not None:
                print(actual.getDato())
                actual = actual.getSiguiente()