import numpy as np
class Cola():
    __items: np.ndarray
    __primero: int
    __ultimo: int
    __cant: int
    __dimension: int

    def __init__(self, dim = 5):
        self.__dimension = dim
        self.__items = np.empty(self.__dimension)
        self.__primero = 0
        self.__ultimo = 0
        self.__cant = 0
    
    def vacia(self):
        return self.__cant == 0

    def insertar(self, elem): 
        if self.__dimension == self.__cant:
            print("No se puede agregar, cola llena")
            return 0
        else:
            self.__items[self.__ultimo] = elem
            self.__ultimo = (self.__ultimo + 1) % self.__dimension
            self.__cant += 1
            return elem

    def suprimir(self):
        if self.vacia():
            print("No se puede suprimir, cola vacia")
            return 0
        else:
            elem = self.__items[self.__primero]
            self.__primero = (self.__primero+1) % self.__dimension
            self.__cant -= 1
            return elem
    
    def recorrer(self):
        if self.vacia():
            print("No se puede recorrer, cola vacia")
            return 0
        else:
            i = self.__primero
            for _ in range(self.__cant):
                print(self.__items[i])
                i = (i + 1) % self.__dimension