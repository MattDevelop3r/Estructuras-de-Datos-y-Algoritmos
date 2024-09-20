from classImpresion import impresion
class Nodo:
    __dato: impresion
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

class Cola:
    __primero: int
    __ultimo: int
    __cant: int
    def __init__(self):
        self.__primero = None
        self.__ultimo = None
        self.__cant = 0
    
    def esta_vacia(self):
        return self.__cant == 0
    
    def insertar(self, elem):
        nuevo_nodo = Nodo(elem)
        if self.esta_vacia():
            self.__primero = nuevo_nodo
            self.__ultimo = nuevo_nodo
        else:
            self.__ultimo.setSiguiente(nuevo_nodo)
            self.__ultimo = nuevo_nodo
        self.__cant += 1
        return elem
    
    def suprimir(self):
        if self.esta_vacia():
            print("No se puede suprimir, cola vacía")
            return None
        else:
            elem = self.__primero.getDato()
            self.__primero = self.__primero.getSiguiente()
            self.__cant -= 1
            if self.__cant == 0:
                self.__ultimo = None
            return elem
    
    def recorrer(self):
        if self.esta_vacia():
            print("No se puede recorrer, cola vacía")
            return None
        else:
            actual = self.__primero
            while actual is not None:
                print(actual.getDato())
                actual = actual.getSiguiente()
    
    def getCantidad(self):
        return self.__cant