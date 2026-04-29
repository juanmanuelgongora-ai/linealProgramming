"""
PROBLEMA DE PROGRAMACIÓN LINEAL #2
====================================
Una carpintería fabrica Mesas (x1) y Sillas (x2).

- Cada Mesa da $8 de ganancia
- Cada Silla da $5 de ganancia

Restricciones:
  1. Madera:   4*x1 + 2*x2 <= 60  (tablas disponibles)
  2. Trabajo:  2*x1 + 3*x2 <= 48  (horas de mano de obra)
  3. x1 >= 0,  x2 >= 0

Objetivo: Maximizar Z = 8*x1 + 5*x2
"""

from scipy.optimize import linprog

# --- Función objetivo (negada porque linprog MINIMIZA) ---
c = [-8, -5]

# --- Restricciones (<=) ---
A = [[4, 2],   # Madera
     [2, 3]]   # Trabajo

b = [60, 48]

# --- Límites: x1 >= 0, x2 >= 0 ---
limites = [(0, None), (0, None)]

# --- Resolver ---
resultado = linprog(c, A_ub=A, b_ub=b, bounds=limites, method='highs')

# --- Mostrar resultados ---
print("PROBLEMA: Carpintería - Maximizar ganancias")
print("=============================================")
print(f"Mesas a producir   (x1) = {resultado.x[0]:.0f} unidades")
print(f"Sillas a producir  (x2) = {resultado.x[1]:.0f} unidades")
print(f"Ganancia máxima    (Z)  = ${-resultado.fun:.0f}")
