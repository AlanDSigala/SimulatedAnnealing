import math
import random

# Función objetivo: f(x) = x^4 + 3x^3 + 2x^2 - 1, f(x)= x^2 - 3x - 8
def funcion_objetivo(x):
    return x**2 + 3*x -8

# Genera una solución vecina realizando un pequeño cambio en x
def generar_solucion_vecina(solucion_actual):
    delta_x = random.uniform(-1.0, 1.0)  
  
    return solucion_actual + delta_x

# Parámetros del algoritmo
temperatura_inicial = 100.0
tasa_enfriamiento = 0.95
numero_iteraciones = 1000

# Solución inicial aleatoria 
solucion_actual = random.uniform(-2, 2)

# Mejor solución encontrada
mejor_solucion = solucion_actual
mejor_valor_objetivo = funcion_objetivo(solucion_actual)

for i in range(numero_iteraciones):
    # Genera una solución vecina
    solucion_vecina = generar_solucion_vecina(solucion_actual)
    
    # Calcula la diferencia en el valor de la función objetivo
    diferencia = funcion_objetivo(solucion_vecina) - funcion_objetivo(solucion_actual)

  
    # Si la solución vecina es mejor, acéptala
    if diferencia < 0:
        solucion_actual = solucion_vecina
    else:
        # Calcula la probabilidad de aceptación
        probabilidad_aceptacion = math.exp(-diferencia / temperatura_inicial)
        
        # Acepta la solución vecina con una cierta probabilidad
        if random.random() < probabilidad_aceptacion:
            solucion_actual = solucion_vecina
    
    # Actualiza la temperatura
    temperatura_inicial *= tasa_enfriamiento
    
    # Actualiza la mejor solución si es necesario
    valor_objetivo_actual = funcion_objetivo(solucion_actual)
    if valor_objetivo_actual < mejor_valor_objetivo:
        mejor_solucion = solucion_actual
        mejor_valor_objetivo = valor_objetivo_actual

# La mejor solución encontrada
print("Mejor solución (x):", mejor_solucion)
print("Valor de la función objetivo (f(x)):", mejor_valor_objetivo)
