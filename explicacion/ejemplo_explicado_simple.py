"""
================================================================================
EJEMPLO EXPLICADO - Versión Simple
================================================================================

PROBLEMA:
========
Una panadería produce:
  - Pan (x1)
  - Galletas (x2)

Cada Pan да $5 de ganancia
Cada Galleta да $3 de ganancia

Recursos disponibles:
  - Harina: 40 kilos (se usan 2 para cada pan, 1 para cada galleta)
  - Horno: 30 horas (se usa 1 para cada producto)

Objetivo: Maximizar la ganancia

================================================================================
"""

# Importar la función que resuelve problemas de programación lineal
from scipy.optimize import linprog

# ============================================================
# Paso 1: Definir la función objetivo
# ============================================================
# Queremos: Maximizar 5*x1 + 3*x2
# Pero la función linprog solo puede MINIMIZAR
# Por eso cambiamos el signo (multiplicamos por -1)
# Queda: Minimizar -5*x1 - 3*x2

c = [-5, -3]

# ============================================================
# Paso 2: Definir las restricciones
# ============================================================
# Restricción 1 (Harina): 2*x1 + 1*x2 <= 40
# Restricción 2 (Horno):  1*x1 + 1*x2 <= 30

# A es una lista con las dos restricciones
A = [
    [2, 1],   # Primera fila: 2*x1 + 1*x2
    [1, 1]    # Segunda fila: 1*x1 + 1*x2
]

# b es una lista con los límites de cada restricción
b = [40, 30]

# ============================================================
# Paso 3: Definir que las variables no pueden ser negativas
# ============================================================
# x1 >= 0 y x2 >= 0
# Cada tupla dice (valor_minimo, valor_maximo)
# None significa "sin límite"

limites = [(0, None), (0, None)]

# ============================================================
# Paso 4: Resolver el problema
# ============================================================
resultado = linprog(c, A_ub=A, b_ub=b, bounds=limites, method='highs')

# ============================================================
# Paso 5: Mostrar los resultados
# ============================================================
print("======================================")
print("RESULTADO DEL PROBLEMA")
print("======================================")
print("")

# Obtener la cantidad de cada producto
x1 = resultado.x[0]  # Cantidad de Pan
x2 = resultado.x[1]  # Cantidad de Galletas

# Convertir a número entero (sin decimales)
x1_entero = int(x1)
x2_entero = int(x2)

# Calcular la ganancia máxima
# Como la función objetivo estaba negada, el resultado aussi está negado
# Por eso negamos otra vez para obtener el valor real
ganancia = int(-resultado.fun)

# Mostrar cada resultado en una línea separada
print("Cantidad de PAN (x1)     =")
print(x1_entero)
print("")

print("Cantidad de GALLETAS (x2) =")
print(x2_entero)
print("")

print("Ganancia maxima =")
print(ganancia)
print("")

# ============================================================
# Verificación
# ============================================================
print("======================================")
print("VERIFICACIÓN")
print("======================================")
print("")

# Calcular cuánto recurso se usa
harina_usada = 2 * x1_entero + 1 * x2_entero
horno_usado = 1 * x1_entero + 1 * x2_entero

print("Harina usada:")
print(harina_usada)
print("(Limite: 40)")
print("")

print("Horno usado:")
print(horno_usado)
print("(Limite: 30)")
print("")

# Nombre de las variables para mostrar
print("======================================")
print("Explicacion de las variables")
print("======================================")
print("")
print("c = [-5, -3]")
print("  Es la funcion objetivo negada")
print("  -5 es el coef. de x1 (Pan)")
print("  -3 es el coef. de x2 (Galletas)")
print("")
print("A = [[2,1],[1,1]]")
print("  Es la matriz de restricciones")
print("  Fila 1: Harina")
print("  Fila 2: Horno")
print("")
print("b = [40, 30]")
print("  Son los limites de cada restriccion")
print("")
print("limites = [(0,None),(0,None)]")
print("  x1 >= 0 y x2 >= 0")
print("  (No se puede producir negativo)")