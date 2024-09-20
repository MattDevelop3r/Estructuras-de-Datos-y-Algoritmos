import numpy as np
class Nodo():
    __dato: int
    __siguiente: int

    def __init__(self):
        self.__siguiente = -2

    def setDato(self, x):
        self.__dato = x
    
    def getDato(self):
        return self.__dato
    
    def setSiguiente(self, xp):
        self.__siguiente = xp
    
    def getSiguiente(self):
        return self.__siguiente
    
class lista():
    __max: int
    __cab: int
    __cant: int
    __espacio: np.ndarray
    __disponible: int

    def __init__(self, xmax):
        self.__max = xmax
        self.__cab = 0
        self.__cant = 0
        self.__espacio = np.empty(self.__max, dtype= Nodo)
        self.__disponible = 0

    def vacia(self):
        return self.__cant == 0
    
    def getDisponible(self):
        i = 0
        while i < max and self.__espacio[i].getSiguiente() != -2:
            i += 1
        if i < max:
            self.__disponible = i
            bandera = True
        else: 
            self.__disponible = -2
            bandera = False
        return bandera
        
    def freeDisponible(self):
        if self.__disponible >= 0 and self.__disponible < self.__max:
            self.__espacio[self.__disponible].setSiguiente(-2)
            bandera = True
        else:
            bandera = False
        return bandera
    
    def insertarPorPosicion(self, x, xp): #inserta por posicion
        if self.__cant < self.__max and xp >= 0 and xp <= self.__cant and self.getDisponible():
            self.__espacio[self.__disponible].setDato(x)
            ant = self.__cab
            cabeza = self.__cab
            i = 0
            while i < xp:
                i += 1
                ant = cabeza
                cabeza = self.__espacio[cabeza].getSiguiente()
            if cabeza == self.__cab: #inserta al inicio
                if self.__cant == 0: #inserta en la lista vacia
                    self.__espacio[self.__cab].setSiguiente(-1)
                else:  #inserta en la lista con elementos
                    self.__espacio[self.__disponible].setSiguiente(self.__cab)
                self.__cab = self.__disponible
            elif cabeza == -1: #inserta al final de la lista
                self.__espacio[self.__disponible].setSiguiente(-1)
                self.__espacio[ant].setSiguiente(self.__disponible)
            else: #inserta en otro lado
                self.__espacio[self.__disponible].setSiguiente(cabeza)
                self.__espacio[ant].setSiguiente(self.__disponible)
            self.__cab += 1
            return True
        else:
            print("Espacio lleno o posicion incorrecta")
            return False
        
    def insertarPorContenido(self, x): #inserta por contenido
        if self.__cant < self.__max and self.getDisponible():
            ant = self.__cab
            cabeza = self.__cant
            i = 0
            self.__espacio[self.__disponible].setDato(x)
            while i < self.__cant and cabeza != -1 and self.__espacio[cabeza].getDato() < x:
                i+=1
                ant = cabeza 
                cabeza = self.__espacio[cabeza].getSiguiente()
            if cabeza == self.__cab: #inserta al inicio de la lista
                if self.__cant == 0: #inserta en la lista vacia
                    self.__espacio[self.__cab].setSiguiente(-1)
                else: #inserta en la lista con elementos
                    self.__espacio[self.__disponible].setSiguiente(self.__cab)
                    self.__cab = self.__disponible
            elif cabeza == -1: #inserta al final de la lista
                self.__espacio[self.__disponible].setSiguiente(-1)
                self.__espacio[ant].setSiguiente(self.__disponible)
            else: #inserta al medio
                self.__espacio[self.__disponible].setSiguiente(cabeza)
                self.__espacio[ant].setSiguiente(self.__disponible)
        
            self.__cant += 1
            return True
        else: 
            print("Espacio lleno")
            return False

    def suprimir(self, xp):
        if self.__cant != 0 and xp >= 0 and xp < self.__cant:
            ant = self.__cab
            cabeza = self.__cab 
            i = 0
            while i < xp and cabeza != -1:
                i += 1
                ant = cabeza
                cabeza = self.__espacio[cabeza].getSiguiente()
            
            if cabeza == self.__cab:
                if self.__cant == 1:
                    self.__cab = 0
                else: 
                    self.__cab = self.__espacio[ant].getSiguiente()
            else: 
                self.__espacio[ant].setSiguiente(self.__espacio[cabeza].getSiguiente())
                x = self.__espacio[cabeza].getDato()
                self.__disponible = cabeza
                self.freeDisponible(self.__disponible)
                self.__cant -= 1
                return True
        else: 
            print("Lista vacia o posicion incorrecta")
            return False

    def recuperar(self, xp):
        if self.__cant != 0 and xp >= 0 and xp < self.__cant:
            cabeza = self.__cab
            i = 0
            while cabeza != -1 and i < xp:
                i += 1
                cabeza = self.__espacio[cabeza].getSiguiente()
            return self.__espacio[cabeza].getDato()
        else:
            print("Lista vacía o posición incorrecta.")
            return None

    def buscar(self, x):
        if self.__cant != 0:
            cabeza = self.__cab
            i = 0
            while i < self.__cant and cabeza != -1 and self.__espacio[cabeza].getDato() != x:
                i += 1
                cabeza = self.__espacio[cabeza].getSiguiente()
            if i < self.__cant:
                return i + 1
            else:
                return None
        else:
            print("Lista vacía.")
            return None

    def primerElemento(self):
        if self.__cant != 0:
            return self.__espacio[self.__cab].getDato()
        else:
            print("Lista vacía.")
            return None

    def ultimoElemento(self):
        if self.__cant != 0:
            cabeza = self.__cab
            aux = 0
            while cabeza != -1:
                aux = self.__espacio[cabeza].getDato()
                cabeza = self.__espacio[cabeza].getSiguiente()
            return aux
        else:
            print("Lista vacía.")
            return None

    def siguientePosicion(self, xp):
        if self.__cant != 0 and xp >= 0 and xp < self.__cant - 1:
            return xp + 2
        else:
            print("Lista vacía o último elemento.")
            return None

    def anteriorPosicion(self, xp):
        if self.__cant != 0 and xp > 0 and xp < self.__cant:
            return xp
        else:
            print("Lista vacía o primer elemento.")
            return None

    def recorrer(self):
        if self.__cant != 0:
            cabeza = self.__cab
            print("Lista:", end=" ")
            while cabeza != -1:
                print(self.__espacio[cabeza].getDato(), end=" ")
                cabeza = self.__espacio[cabeza].getSiguiente()
            print()
            return True
        else:
            print("Lista vacía.")
            return False

    def sucesor(self, x):
        p1 = self.buscar(x)
        if p1 is not None:
            p2 = self.siguientePosicion(p1)
            if p2 is not None:
                return self.recuperar(p2)
        return None

    def predecesor(self, x):
        p1 = self.buscar(x)
        if p1 is not None:
            p2 = self.anteriorPosicion(p1)
            if p2 is not None:
                return self.recuperar(p2)
        return None