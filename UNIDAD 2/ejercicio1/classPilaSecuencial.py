import numpy as np

class Pila():
    __items: np.ndarray
    __tope: int
    __cant: int
    __dimension: int
    
    def __init__(self, dim = 5):
        self.__tope = -1
        self.__cant = 0
        self.__dimension = dim
        self.__items = np.empty(self.__dimension)
    
    def vacia(self):
        return self.__tope == -1
    
    def insertar(self, elem):
        if self.__dimension == self.__cant:
            print("La pila está llena, no se puede agregar")
        else: 
            self.__items[self.__tope + 1] = elem
            self.__tope += 1
            self.__cant += 1
            return elem
        
    def suprimir(self):
        if self.vacia():
            print("La pila está vacía, no se puede eliminar")
        else:
            elem = self.__items[self.__tope]
            self.__tope -= 1 
            self.__cant -= 1
            return elem
    
    def recorrer(self):
        if self.vacia():
            print("No se puede recorrer, pila vacía")
            return None
        else:
            actual = self.__tope
            i = self.__tope
            for _ in range(self.__cant):
                print(self.__items[i])
                i -= 1

	    
    
