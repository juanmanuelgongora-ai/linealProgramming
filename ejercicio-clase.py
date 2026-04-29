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
#paso 1
from scipy.optimize import linprog

#paso 2
#definir la funcion objetivo

c = [-5, -3]

# paso 3
#definir reastricciones
A = [[2,1],
    [1,1]
]

#paso 4
#limite de restricciones
b = [40, 30]

#paso 5
#definir variables minimas y maximas

limite = [(0,None), (0,None)]

#paso 6 
#calculo
resultado = linprog(
  c, #funcion objetivo
  A_ub = A, #restricciones
  b_ub = b, # limites de las restricciones
  bounds = limites, #limites
  method = 'highs'
)

#paso 7
#mostrar resultados

x1 = resultado.x[0]
x2 = resultado.x[1]

ganancia = int(-resultado.fun)


print("cantidad pan: ", x1)
print("cantidad galletas: ", x2)

print("ganancia adquirida: ", ganancia)