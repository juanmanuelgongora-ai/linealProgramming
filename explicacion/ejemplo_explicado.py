"""
================================================================================
PROBLEMA DE PROGRAMACIÓN LINEAL - EXPLICACIÓN DETALLADA
================================================================================

ESCENARIO DEL PROBLEMA:
=====================
Una panadería produce dos productos:
  - Pan (llamaremos a esta variable x1)
  - Galletas (llamaremos a esta variable x2)

GANANCIAS POR CADA PRODUCTO:
  - Cada Pan vendidosgenera $5 de ganancia
  - Cada Galleta vendidas genera $3 de ganancia

RECURSOS QUE TIENE LA PANADERÍA:
  1. HARINA: 
     - Para hacer 1 Pan se necesitan 2 kilos de harina
     - Para hacer 1 Galleta se necesita 1 kilo de harina
     - Tiene 40 kilos de harina disponibles
     -Se resume como: 2*x1 + 1*x2 <= 40

  2. HORNO:
     - Para hacer 1 Pan se necesita 1 hora de horno
     - Para hacer 1 Galleta se necesita 1 hora de horno
     - Tiene 30 horas de horno disponibles
     - Se resume como: 1*x1 + 1*x2 <= 30

  3. No se puede producir cantidad negativa:
     - x1 debe ser mayor o igual a 0
     - x2 debe ser mayor o igual a 0

FUNCIÓN OBJETIVO (qué queremos maximizar):
  Ganancia total = 5*x1 + 3*x2

================================================================================
"""

# ==============================================================================
# IMPORTAR BIBLIOTECA
# ==============================================================================
# linprog es una función de la biblioteca scipy que resuelve problemas
# de programación lineal

from scipy.optimize import linprog

# ==============================================================================
# DEFINIR LA FUNCIÓN OBJETIVO
# ==============================================================================
# La función objetivo es: Maximizar 5*x1 + 3*x2
# Pero linprog solo puede MINIMIZAR, no maximiza
# Por eso multiplicamos todo por -1 para cambiar maximización por minimización
# Original: Maximizar 5*x1 + 3*x2
# Convertido: Minimizar -5*x1 - 3*x2

c = [-5, -3]

# ==============================================================================
# DEFINIR LAS RESTRICCIONES
# ==============================================================================
# Primera restricción (HARINA): 2*x1 + 1*x2 <= 40
# Segunda restricción (HORNO):  1*x1 + 1*x2 <= 30

A = [
    [2, 1],   # Línea 1: Restricción de HARINA
    [1, 1]    # Línea 2: Restricción de HORNO
]

#limites de cada restriccion
b = [40, 30]

# ==============================================================================
# DEFINIR QUE LAS VARIABLES NO PUEDEN SER NEGATIVAS
# ==============================================================================
# x1 >= 0 significa que el valor mínimo de x1 es 0
# x2 >= 0 significa que el valor mínimo de x2 es 0

limites = [(0, None), (0, None)]
#cada tupla define el valor minimo y maximo de cada variable
#None significa sin limite

# ==============================================================================
# RESOLVER EL PROBLEMA
# ==============================================================================
resultado = linprog(
    c,           # Función objetivo
    A_ub=A,      # Matriz de restricciones
    b_ub=b,       # Límites de las restricciones
    bounds=limites,
    method='highs'
)

# ==============================================================================
# MOSTRAR LOS RESULTADOS
# ==============================================================================
print("=" * 50)
print("PROBLEMA: Panadería - Maximizar ganancias")
print("=" * 50)
print()

# Obtener los valores de las variables
x1 = resultado.x[0]  # Cantidad de Pan
x2 = resultado.x[1]  # Cantidad de Galletas

# Convertir a números enteros (sin decimales)
x1_entero = int(x1)
x2_entero = int(x2)

# Calcular la ganancia máxima
# Negamos el resultado porque también estaba negada la función objetivo
ganancia = int(-resultado.fun)

print("Cantidad óptima de PAN (x1)      =", x1_entero, "unidades")
print("Cantidad óptima de GALLETAS (x2) =", x2_entero, "unidades")
print()
print("GANANCIA MÁXIMA (Z)             = $", ganancia)
print()

# ==============================================================================
# VERIFICACIÓN (comprobar que la solución es correcta)
# ==============================================================================
print("Verificación:")
print("  - Harina usada: 2*x1 + 1*x2 = 2*", x1_entero, "+ 1*", x2_entero, "=", 2*x1_entero + 1*x2_entero, "(límite: 40)")
print("  - Horno usado: 1*x1 + 1*x2 = 1*", x1_entero, "+ 1*", x2_entero, "=", 1*x1_entero + 1*x2_entero, "(límite: 30)")