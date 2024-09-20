class Nodo:
    __clave: int
    __izquierda: 'Nodo'
    __derecha: 'Nodo'

    def __init__(self, clave):
        self.__clave = clave
        self.__izquierda = None
        self.__derecha = None

    # Métodos para obtener y asignar la clave
    def getClave(self):
        return self.__clave

    def setClave(self, clave):
        self.__clave = clave

    # Métodos para obtener y asignar el nodo izquierdo
    def getIzquierda(self):
        return self.__izquierda

    def setIzquierda(self, valor):
        self.__izquierda = valor

    # Métodos para obtener y asignar el nodo derecho
    def getDerecha(self):
        return self.__derecha

    def setDerecha(self, valor):
        self.__derecha = valor


class ArbolBinarioBusqueda:
    __raiz: Nodo

    def __init__(self):
        self.__raiz = None

    def insertar(self, clave):
        if self.__raiz is None:
            self.__raiz = Nodo(clave)
            return

        actual = self.__raiz
        while True:
            if clave < actual.getClave():
                if actual.getIzquierda() is None:
                    actual.setIzquierda(Nodo(clave))
                    break
                actual = actual.getIzquierda()
            elif clave > actual.getClave():
                if actual.getDerecha() is None:
                    actual.setDerecha(Nodo(clave))
                    break
                actual = actual.getDerecha()
            else:
                break

    def suprimir(self, clave):
        self.__raiz = self.__suprimirRecursivo(self.__raiz, clave)

    def __suprimirRecursivo(self, raiz, clave):
        if raiz is None:
            return raiz
        if clave < raiz.getClave():
            raiz.setIzquierda(self.__suprimirRecursivo(raiz.getIzquierda(), clave))
        elif clave > raiz.getClave():
            raiz.setDerecha(self.__suprimirRecursivo(raiz.getDerecha(), clave))
        else:
            if raiz.getIzquierda() is None:
                return raiz.getDerecha()
            elif raiz.getDerecha() is None:
                return raiz.getIzquierda()
            temp = self.__nodoValorMinimo(raiz.getDerecha())
            raiz.setClave(temp.getClave())
            raiz.setDerecha(self.__suprimirRecursivo(raiz.getDerecha(), temp.getClave()))
        return raiz

    def __nodoValorMinimo(self, nodo):
        actual = nodo
        while actual.getIzquierda() is not None:
            actual = actual.getIzquierda()
        return actual

    def buscar(self, clave):
        return self.__buscarRecursivo(self.__raiz, clave)

    def __buscarRecursivo(self, raiz, clave):
        if raiz is None or raiz.getClave() == clave:
            return raiz
        if raiz.getClave() < clave:
            return self.__buscarRecursivo(raiz.getDerecha(), clave)
        return self.__buscarRecursivo(raiz.getIzquierda(), clave)

    def nivel(self, clave):
        return self.__nivelRecursivo(self.__raiz, clave, 0)

    def __nivelRecursivo(self, raiz, clave, nivel):
        if raiz is None:
            return -1
        if raiz.getClave() == clave:
            return nivel
        izquierda = self.__nivelRecursivo(raiz.getIzquierda(), clave, nivel + 1)
        if izquierda != -1:
            return izquierda
        return self.__nivelRecursivo(raiz.getDerecha(), clave, nivel + 1)

    def hoja(self, clave):
        nodo = self.buscar(clave)
        return nodo is not None and nodo.getIzquierda() is None and nodo.getDerecha() is None

    def hijo(self, claveHijo, clavePadre):
        padre = self.buscar(clavePadre)
        if padre is None:
            return False
        return (padre.getIzquierda() and padre.getIzquierda().getClave() == claveHijo) or \
               (padre.getDerecha() and padre.getDerecha().getClave() == claveHijo)

    def padre(self, claveHijo, clavePadre):
        return self.hijo(claveHijo, clavePadre)

    def camino(self, claveInicio, claveFin):
        camino = []
        self.__caminoRecursivo(self.__raiz, claveInicio, claveFin, camino)
        return camino if camino else None

    def __caminoRecursivo(self, raiz, claveInicio, claveFin, camino):
        if raiz is None:
            return False
        camino.append(raiz.getClave())
        if raiz.getClave() == claveFin:
            return True
        if (raiz.getIzquierda() and self.__caminoRecursivo(raiz.getIzquierda(), claveInicio, claveFin, camino)) or \
           (raiz.getDerecha() and self.__caminoRecursivo(raiz.getDerecha(), claveInicio, claveFin, camino)):
            return True
        camino.pop()
        return False

    def altura(self):
        return self.__alturaRecursiva(self.__raiz)

    def __alturaRecursiva(self, raiz):
        if raiz is None:
            return -1
        alturaIzquierda = self.__alturaRecursiva(raiz.getIzquierda())
        alturaDerecha = self.__alturaRecursiva(raiz.getDerecha())
        return max(alturaIzquierda, alturaDerecha) + 1

    def inOrden(self):
        resultado = []
        self.__inOrdenRecursivo(self.__raiz, resultado)
        return resultado

    def __inOrdenRecursivo(self, raiz, resultado):
        if raiz:
            self.__inOrdenRecursivo(raiz.getIzquierda(), resultado)
            resultado.append(raiz.getClave())
            self.__inOrdenRecursivo(raiz.getDerecha(), resultado)

    def preOrden(self):
        resultado = []
        self.__preOrdenRecursivo(self.__raiz, resultado)
        return resultado

    def __preOrdenRecursivo(self, raiz, resultado):
        if raiz:
            resultado.append(raiz.getClave())
            self.__preOrdenRecursivo(raiz.getIzquierda(), resultado)
            self.__preOrdenRecursivo(raiz.getDerecha(), resultado)

    def postOrden(self):
        resultado = []
        self.__postOrdenRecursivo(self.__raiz, resultado)
        return resultado

    def __postOrdenRecursivo(self, raiz, resultado):
        if raiz:
            self.__postOrdenRecursivo(raiz.getIzquierda(), resultado)
            self.__postOrdenRecursivo(raiz.getDerecha(), resultado)
            resultado.append(raiz.getClave())
