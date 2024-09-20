class impresion():
    __tiempo_impresion: int
    __tiempo_espera: int

    def __init__(self, tiempoImpresion, tiempoEspera):
        self.__tiempo_impresion = tiempoImpresion
        self.__tiempo_espera = tiempoEspera
    
    def getTiempoImpresion(self):
        return self.__tiempo_impresion
    def getTiempoEspera(self):
        return self.__tiempo_espera
    def setTiempoImpresion(self, t):
        self.__tiempo_impresion = t
    def setTiempoEspera(self, t):
        self.__tiempo_espera = t

