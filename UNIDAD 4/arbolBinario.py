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
    def get__izquierda(self):
        return self.__izquierda

    def set__izquierda(self, valor):
        self.__izquierda = valor

    # Métodos para obtener y asignar el nodo derecho
    def get__derecha(self):
        return self.__derecha

    def set__derecha(self, valor):
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
            if clave < actual.__clave:
                if actual.__izquierda is None:
                    actual.__izquierda = Nodo(clave)
                    break
                actual = actual.__izquierda
            elif clave > actual.__clave:
                if actual.__derecha is None:
                    actual.__derecha = Nodo(clave)
                    break
                actual = actual.__derecha
            else:
                # La clave ya existe en el árbol, no se inserta
                break

    def suprimir(self, clave):
        self.__raiz = self.__suprimirRecursivo(self.__raiz, clave)

    def __suprimirRecursivo(self, raiz, clave):
        if raiz is None:
            return raiz
        if clave < raiz.clave:
            raiz.__izquierda = self.__suprimirRecursivo(raiz.__izquierda, clave)
        elif clave > raiz.clave:
            raiz.__derecha = self.__suprimirRecursivo(raiz.__derecha, clave)
        else:
            if raiz.__izquierda is None:
                return raiz.__derecha
            elif raiz.__derecha is None:
                return raiz.__izquierda
            temp = self.__nodoValorMinimo(raiz.__derecha)
            raiz.Nodo__clave = temp.__clave
            raiz.__derecha = self.__suprimirRecursivo(raiz.__derecha, temp.clave)
        return raiz

    def __nodoValorMinimo(self, nodo):
        actual = nodo
        while actual.__izquierda is not None:
            actual = actual.__izquierda
        return actual

    def buscar(self, clave):
        return self.__buscarRecursivo(self.__raiz, clave)

    def __buscarRecursivo(self, raiz, clave):
        if raiz is None or raiz.__clave == clave:
            return raiz
        if raiz.__clave < clave:
            return self.__buscarRecursivo(raiz.__derecha, clave)
        return self.__buscarRecursivo(raiz.__izquierda, clave)

    def nivel(self, clave):
        return self.__nivelRecursivo(self.__raiz, clave, 0)

    def __nivelRecursivo(self, raiz, clave, nivel):
        if raiz is None:
            return -1
        if raiz.clave == clave:
            return nivel
        __izquierda = self.__nivelRecursivo(raiz.__izquierda, clave, nivel + 1)
        if __izquierda != -1:
            return __izquierda
        return self.__nivelRecursivo(raiz.__derecha, clave, nivel + 1)

    def hoja(self, clave):
        nodo = self.buscar(clave)
        return nodo is not None and nodo.__izquierda is None and nodo.__derecha is None

    def hijo(self, claveHijo, clavePadre):
        padre = self.buscar(clavePadre)
        if padre is None:
            return False
        return (padre.__izquierda and padre.__izquierda.__clave == claveHijo) or (padre.__derecha and padre.__derecha.__clave == claveHijo)

    def padre(self, claveHijo, clavePadre):
        return self.hijo(claveHijo, clavePadre)

    def camino(self, claveInicio, claveFin):
        camino = []
        self.__caminoRecursivo(self.__raiz, claveInicio, claveFin, camino)
        return camino if camino else None

    def __caminoRecursivo(self, raiz, claveInicio, claveFin, camino):
        if raiz is None:
            return False
        camino.append(raiz.__clave)
        if raiz.clave == claveFin:
            return True
        if (raiz.__izquierda and self.__caminoRecursivo(raiz.__izquierda, claveInicio, claveFin, camino)) or \
           (raiz.__derecha and self.__caminoRecursivo(raiz.__derecha, claveInicio, claveFin, camino)):
            return True
        camino.pop()
        return False

    def altura(self):
        return self.__alturaRecursiva(self.__raiz)

    def __alturaRecursiva(self, raiz):
        if raiz is None:
            return -1
        altura__izquierda = self.__alturaRecursiva(raiz.__izquierda)
        altura__derecha = self.__alturaRecursiva(raiz.__derecha)
        return max(altura__izquierda, altura__derecha) + 1

    def inOrden(self):
        resultado = []
        self.__inOrdenRecursivo(self.__raiz, resultado)
        return resultado

    def __inOrdenRecursivo(self, raiz, resultado):
        if raiz:
            self.__inOrdenRecursivo(raiz.__izquierda, resultado)
            resultado.append(raiz.__clave)
            self.__inOrdenRecursivo(raiz.__derecha, resultado)

    def preOrden(self):
        resultado = []
        self.__preOrdenRecursivo(self.__raiz, resultado)
        return resultado

    def __preOrdenRecursivo(self, raiz, resultado):
        if raiz:
            resultado.append(raiz.__clave)
            self.__preOrdenRecursivo(raiz.__izquierda, resultado)
            self.__preOrdenRecursivo(raiz.__derecha, resultado)

    def postOrden(self):
        resultado = []
        self.__postOrdenRecursivo(self.__raiz, resultado)
        return resultado

    def __postOrdenRecursivo(self, raiz, resultado):
        if raiz:
            self.__postOrdenRecursivo(raiz.__izquierda, resultado)
            self.__postOrdenRecursivo(raiz.__derecha, resultado)
            resultado.append(raiz.__clave)