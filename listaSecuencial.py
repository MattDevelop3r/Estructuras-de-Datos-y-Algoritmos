import numpy as np

class listaSecuencial():
    __items: np.ndarray
    __dimension: int
    __ultimo: int
    __cant: int

    def __init__(self, dim = 10):
        self.__dimension = dim
        self.__items = np.empty(self.__dimension, dtype = int)
        self.__ultimo = -1
        self.__cant == 0 

    def vacia(self):
        return self.__cant == 0
    
    def insertarPorContenido(self, elem):
        if self.__cant == self.__dimension:
            print("no se puede insertar, lista llena")
            return
        elif self.vacia():
            self.__items[0] = elem
            
        else: 
            i = 0
            while i < self.__ultimo + 1 and elem < self.__items[i]:
                i += 1
            j = 0
            for j in range(self.__ultimo + 1, i - 1, -1):
                self.__items[j] == self.__items[j+1]
            self.__items[j] = elem
            
        self.__cant += 1
        self.__ultimo += 1
    
    def suprimir

    def recuperar(self, pos):
        if pos > 0 and pos <= self.__ultimo:
            return self.__items[pos]
        else: print("no se pudo recuperar, posicion invalida")
    
    def primer_elem(self):
        return self.__items[0]