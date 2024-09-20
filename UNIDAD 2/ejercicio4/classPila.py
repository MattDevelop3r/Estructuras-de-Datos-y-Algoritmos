import numpy as np

class Pila():
    __items: np.ndarray
    __tope: int
    __cant: int
    __dimension: int
    
    def __init__(self, dim):
        self.__tope = -1
        self.__cant = 0
        self.__dimension = dim
        self.__items = np.empty(self.__dimension, dtype= int)
    
    def vacia(self):
        return self.__tope == -1
    
    def llena(self):
        return self.__cant == self.__dimension
    
    def insertar(self, elem):
        if self.llena():
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

    
    
