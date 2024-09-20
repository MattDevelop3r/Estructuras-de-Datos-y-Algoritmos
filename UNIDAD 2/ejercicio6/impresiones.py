from classImpresion import impresion
from classColaEncadenada import Cola
import random

def generar_trabajo_aleatorio():
    # Genera un trabajo con un tiempo de impresión aleatorio entre 1 y 10 minutos
    tiempo_impresion = random.randint(1, 10)
    return impresion(tiempo_impresion, 0)  # Tiempo de espera inicial es 0

def simular_impresion(num_trabajos: int, tiempo_total: int):
    max_tiempo=5
    cola = Cola()
    trabajos_atendidos = 0
    total_tiempo_espera = 0
    tiempo_simulacion = 0

    # Generar trabajos aleatorios y agregarlos a la cola
    for _ in range(num_trabajos):
        trabajo = generar_trabajo_aleatorio()
        cola.insertar(trabajo)

    # Procesar la cola
    while not cola.esta_vacia() and tiempo_simulacion < tiempo_total:
        trabajo_actual = cola.suprimir()

        # Actualizar tiempo de espera del trabajo
        tiempo_espera = trabajo_actual.getTiempoEspera() + tiempo_simulacion
        trabajo_actual.setTiempoEspera(tiempo_espera)

        tiempo_restante = trabajo_actual.getTiempoImpresion()

        # Si el tiempo de impresión es mayor al máximo, reingresar el trabajo
        if tiempo_restante > max_tiempo:
            tiempo_restante -= max_tiempo
            trabajo_actual.setTiempoImpresion(tiempo_restante)
            cola.insertar(trabajo_actual)  # Volver a la cola
        else:
            # El trabajo fue completado
            trabajos_atendidos += 1
            total_tiempo_espera += trabajo_actual.getTiempoEspera()

        tiempo_simulacion += max_tiempo  # Simulamos que han pasado 5 minutos

    # Calcular el promedio de espera de los trabajos atendidos
    if trabajos_atendidos > 0:
        promedio_espera = total_tiempo_espera / trabajos_atendidos
    else:
        promedio_espera = 0
    
    # Resultados
    print(f"Para {num_trabajos} de trabajos y un tiempo total de {tiempo_total} se obtuvo: \f")
    print(f"Trabajos atendidos: {trabajos_atendidos}")
    print(f"Promedio de espera: {promedio_espera} minutos")
    print(f"Tiempo de simulacion: {tiempo_simulacion} minutos")
    print(f"Trabajos sin atender: {cola.getCantidad()}")

if __name__ == '__main__':
    simular_impresion(num_trabajos=15, tiempo_total = 100)
