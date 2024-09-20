import time
from listaSecuencial import ListaSecuencial
from random import randint

def inicializa_matriz(matriz, orden):
    start_time = time.time()  # Comienza el cronómetro
    for i in range(orden * orden):
        numeroRandom = randint(0, 1)
        matriz.Insertar(numeroRandom, i)
    end_time = time.time()  # Detiene el cronómetro
    print(f"Tiempo de ejecución de inicializa_matriz: {end_time - start_time:.4f} segundos")

def sumar_matrices(A, B, orden):
    start_time = time.time()  # Comienza el cronómetro
    matrizSuma = ListaSecuencial(orden * orden)
    for i in range(orden):
        for j in range(orden):
            valorA = A.Recuperar(i * orden + j)  
            valorB = B.Recuperar(i * orden + j)  
            suma = valorA + valorB
            matrizSuma.Insertar(suma, i * orden + j) 
    end_time = time.time()  # Detiene el cronómetro
    print(f"Tiempo de ejecución de sumar_matrices: {end_time - start_time:.4f} segundos")
    return matrizSuma

def muestra_matriz(matriz, orden):
    start_time = time.time()  # Comienza el cronómetro
    for i in range(orden):
        fila = []
        for j in range(orden):
            fila.append(matriz.Recuperar(i * orden + j))
        print(" ".join(map(str, fila)))
    end_time = time.time()  # Detiene el cronómetro
    print(f"Tiempo de ejecución de muestra_matriz: {end_time - start_time:.4f} segundos")

if __name__ == '__main__':
    orden = 20
    matrizA = ListaSecuencial(orden * orden)
    matrizB = ListaSecuencial(orden * orden)
    
    # Inicializa matrices con valores aleatorios
    inicializa_matriz(matrizA, orden)
    inicializa_matriz(matrizB, orden)
    
    # Suma las matrices
    matrizSuma = sumar_matrices(matrizA, matrizB, orden)
    
    # Muestra la matriz resultante
    print("Matriz A:")
    muestra_matriz(matrizA, orden)
    
    print("\nMatriz B:")
    muestra_matriz(matrizB, orden)
    
    print("\nMatriz Suma:")
    muestra_matriz(matrizSuma, orden)
