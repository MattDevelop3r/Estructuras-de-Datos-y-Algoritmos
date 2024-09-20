import numpy as np
class ListaSecuencial:
    __tamanio: int
    __ultimo: int
    __arreglo: np.ndarray
    __cantidad: int
    
    def __init__(self, tamanio = 5):
        self.__tamanio = tamanio
        self.__ultimo = -1
        self.__cantidad = 0
        self.__arreglo = np.empty(self.__tamanio,dtype=int)
        
    def Vacio(self):
        return (self.__cantidad == 0)
    
    def Lleno(self):
        return self.__cantidad == self.__tamanio
    
    def Insertar(self, L,posicion):
        if not self.Lleno():
            if (posicion>=0) and (posicion<=self.__ultimo+1):
                i = self.__ultimo + 1
                while i > posicion:
                    self.__arreglo[i] = self.__arreglo[i-1]
                    i -= 1
                self.__arreglo[i] = L
                self.__cantidad += 1
                self.__ultimo += 1
            else:
                print("La posicion no es valida. La ultima posicion valida es {}".format(self.__ultimo+1))
        else:
            print("No hay mas espacio para insertar mas elementos")

    def Recorrer(self):
        i = 0
        if not self.Vacio():
            while i <= self.__ultimo:
                print("El elemento {}, posicion {}".format(self.__arreglo[i], i))
                i += 1
        else:
            print("La lista esta vacia, no se muestra ningun elemento")
    
    def Recuperar(self, posicion):
        if posicion < 0 or posicion >= self.__cantidad:
            print("Posición no válida")
            return None
        else:
            return self.__arreglo[posicion]
                
    def Suprimir(self,posicion):
        if not self.Vacio():
            if posicion>=0 and posicion<=self.__ultimo:
                i = self.__ultimo
                eliminado = self.__arreglo[posicion]
                while posicion<i:
                    self.__arreglo[posicion] = self.__arreglo[posicion+1]
                    posicion += 1
                self.__cantidad -= 1
                self.__ultimo -= 1
                print("Se elimino el elemento {}".format(eliminado))
            else:
                print("No se puede eliminar, posicion invalida")
        else:
            print("La lista esta vacia, no se puede eliminar ningun elemento")
            
    def Buscar(self,buscado):
        if not self.Vacio():
            i = 0
            while buscado != self.__arreglo[i] and i < self.__ultimo:
                i += 1
            if buscado == self.__arreglo[i]:
                print("El elemento {} esta en la posicion {}".format(buscado,i))
            else:
                print("El elemento {} no esta en la lista".format(buscado))
                
    def PrimerElemento(self):
        if not self.Vacio():
            return self.__arreglo[0]
        
    def UltimoElemento(self):
        if not self.Vacio():
            return self.__arreglo[self.__ultimo]
        
    def Siguiente(self,posicion):
        if not self.Vacio():
            if posicion == self.__ultimo:
                print("En esa posicion esta el ultimo elemento, no tiene siguiente")
            else:
                if posicion >= 0 and posicion < self.__ultimo:
                    print("El siguiente es: {}".format(self.__arreglo[posicion + 1])) 
            
    def Anterior(self,posicion):
        if not self.Vacio():
            if posicion == 0:
                print("En esa posicion se encuentra el primer elemento, no tiene anterior")
            else:
                if posicion > 0 and posicion <= self.__ultimo:
                    print("El anterior es: {}".format(self.__arreglo[posicion - 1])) 
        
        