import time
from listaEnlazada import ListaEnlazada
from classCelda import Celda
from random import randint

def inicializa_matriz(matriz, orden):
    start_time = time.time()  # Comienza el cronómetro
    k = 0
    for i in range(orden):
        for j in range(orden):
            numeroRandom = randint(0, 1)
            if numeroRandom != 0:  # Solo insertar si el valor no es cero
                nueva_celda = Celda(numeroRandom, i + 1, j + 1)
                matriz.Insertar(nueva_celda, k)
                k += 1
    end_time = time.time()  # Detiene el cronómetro
    print(f"Tiempo de ejecución de inicializa_matriz: {end_time - start_time:.4f} segundos")

def muestra_matriz(matriz, orden):
    start_time = time.time()  # Comienza el cronómetro
    cantidad = orden * orden
    k = 0 
    for i in range(1, orden + 1): 
        for j in range(1, orden + 1):
            if k < cantidad: 
                celda = matriz.Recuperar(k)  
                if celda is not None and celda.getFila() == i and celda.getCol() == j:  
                    print(celda.getValor(), end=" ") 
                    k += 1 
                else:
                    print(0, end=" ") 
            else:
                print(0, end=" ") 
        print() 
    end_time = time.time()  # Detiene el cronómetro
    print(f"Tiempo de ejecución de muestra_matriz: {end_time - start_time:.4f} segundos")

def suma_matrices(A, B, C, orden):
    start_time = time.time()  # Comienza el cronómetro
    k = 0
    for i in range(1, orden + 1):
        for j in range(1, orden + 1):
            valorA = 0
            valorB = 0
            
            # Buscar el valor en la matriz A
            band = False
            x = 0
            while x < orden * orden and not band:
                celdaA = A.Recuperar(x)
                if celdaA is None:
                    break
                if celdaA.getFila() == i and celdaA.getCol() == j:
                    valorA = celdaA.getValor()
                    band = True
                x += 1
            
            # Buscar el valor en la matriz B
            band = False
            x = 0
            while x < orden * orden and not band:
                celdaB = B.Recuperar(x)
                if celdaB is None:
                    break
                if celdaB.getFila() == i and celdaB.getCol() == j:
                    valorB = celdaB.getValor()
                    band = True
                x += 1
            
            # Sumar los valores y crear una nueva celda si el resultado no es cero
            suma = valorA + valorB
            if suma != 0:
                nueva_celda = Celda(suma, i, j)
                C.Insertar(nueva_celda, k)
                k += 1
    end_time = time.time()  # Detiene el cronómetro
    print(f"Tiempo de ejecución de suma_matrices: {end_time - start_time:.4f} segundos")

if __name__ == '__main__':
    matrizA = ListaEnlazada()
    matrizB = ListaEnlazada()
    matrizSuma = ListaEnlazada()

    orden = 20

    inicializa_matriz(matrizA, orden)
    inicializa_matriz(matrizB, orden)

    print("\nLa matriz A es esta: ")
    muestra_matriz(matrizA, orden)

    print("\nLa matriz B es esta: ")
    muestra_matriz(matrizB, orden)

    suma_matrices(matrizA, matrizB, matrizSuma, orden)

    print("\nLa matriz suma resultante es: ")
    muestra_matriz(matrizSuma, orden)
