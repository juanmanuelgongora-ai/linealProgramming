"""
PROBLEMA DE PROGRAMACIÓN LINEAL
================================
Una panadería produce Pan (x1) y Galletas (x2).

- Cada Pan da $5 de ganancia
- Cada Galleta da $3 de ganancia

Restricciones:
  1. Harina: 2*x1 + 1*x2 <= 40  (kilos de harina disponibles)
  2. Horno:  1*x1 + 1*x2 <= 30  (horas de horno disponibles)
  3. x1 >= 0,  x2 >= 0

Objetivo: Maximizar Z = 5*x1 + 3*x2
"""

from scipy.optimize import linprog

# --- Función objetivo (negada porque linprog MINIMIZA) ---
c = [-5, -3]

# --- Restricciones (<=) ---
A = [[2, 1],   # Harina
     [1, 1]]   # Horno

b = [40, 30]

# --- Límites: x1 >= 0, x2 >= 0 ---
limites = [(0, None), (0, None)]

# --- Resolver ---
resultado = linprog(c, A_ub=A, b_ub=b, bounds=limites, method='highs')

# --- Mostrar resultados ---
print("PROBLEMA: Panadería - Maximizar ganancias")
print("==========================================")
print(f"Pan a producir      (x1) = {resultado.x[0]:.0f} unidades")
print(f"Galletas a producir (x2) = {resultado.x[1]:.0f} unidades")
print(f"Ganancia máxima     (Z)  = ${-resultado.fun:.0f}")
