class Celda:
    __valor: int
    __fila: int
    __columna: int

    def __init__(self, valor, fila, col):
        self.__valor = valor
        self.__fila = fila
        self.__columna = col
    
    def getValor(self):
        return self.__valor
    
    def getFila(self):
        return self.__fila
    
    def getCol(self):
        return self.__columna