"""
================================================================================
EJERCICIO EXTRA - PROGRAMACIÓN LINEAL
================================================================================

ENUNCIADO:
=========
Una carpintería fabrica dos productos:

MESAS (x1):
  - Cada mesa да $8 de ganancia
  - Se necesitan 4 tablas de madera
  - Se necesitan 2 horas de trabajo

SILLAS (x2):
  - Cada silla да $5 de ganancia
  - Se necesitan 2 tablas de madera
  - Se necesitan 3 horas de trabajo

RECURSOS DISPONIBLES:
  - Madera total: 60 tablas
  - Tiempo de trabajo total: 48 horas

RESTRICCIONES:
  - No se puede producir cantidad negativa
  - x1 >= 0, x2 >= 0

PREGUNTAS:
=========
1. ¿Cuántas mesas se deben producir?
2. ¿Cuántas sillas se deben producir?
3. ¿Cuál es la ganancia máxima?

FÓRMULA DEL PROBLEMA:
====================
Maximizar: Z = 8*x1 + 5*x2

Sujeto a:
  4*x1 + 2*x2 <= 60   (restricción de madera)
  2*x1 + 3*x2 <= 48   (restricción de tiempo)
  x1 >= 0, x2 >= 0   (no negatividad)
"""

# Resolver usando Python

from scipy.optimize import linprog

# Función objetivo: Maximizar 8*x1 + 5*x2
# La negamos para que linprog pueda minimizarla
c = [-8, -5]

# Restricciones:
# Madera: 4*x1 + 2*x2 <= 60
# Tiempo: 2*x1 + 3*x2 <= 48
A = [
    [4, 2],   # Madera
    [2, 3]    # Tiempo
]

b = [60, 48]

# Variables no negativas
limites = [(0, None), (0, None)]

# Resolver
resultado = linprog(c, A_ub=A, b_ub=b, bounds=limites, method='highs')

# Mostrar resultados
print("=" * 50)
print("SOLUCIÓN - Carpintería")
print("=" * 50)
print()

# Obtener valores
x1 = int(resultado.x[0])
x2 = int(resultado.x[1])
ganancia = int(-resultado.fun)

print("Mesas a producir (x1)  =", x1)
print("Sillas a producir (x2) =", x2)
print("Ganancia máxima         = $", ganancia)
print()

# Verificación
print("Verificación:")
print("  Madera usada: 4*", x1, "+ 2*", x2, "=", 4*x1 + 2*x2, "(límite: 60)")
print("  Tiempo: 2*", x1, "+ 3*", x2, "=", 2*x1 + 3*x2, "(límite: 48)")