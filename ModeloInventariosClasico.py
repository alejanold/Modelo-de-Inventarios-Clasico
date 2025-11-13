# Modelo de Inventarios EOQ Clásico
# Autor: Ale Ortiz
# Ingeniería en Sistemas Computacionales - 3er semestre

import math

print("==== MODELO DE INVENTARIOS EOQ CLÁSICO ====\n")

# Aquí pediré los datos para aplicar el modelo
costo_pedido = float(input("Ingresa el costo de pedido (K): "))
demanda = float(input("Ingresa la demanda del producto (D): "))
costo_almacenamiento = float(input("Ingresa el costo de almacenamiento y proceso (h): "))
dias_entrega = float(input("Ingrese en cuántos días recibes tu pedido (L): "))

print("\n=== Aqui va el paso a paso ===")

# Parte 1: punto optimo de pedido (y*)
# Formula: y* = √(2 * D / h)
# Segun yo aqui con este dato se indica la cantidad que conviene pedir :P
print("\n1) Cálculo del punto óptimo de pedido (y*)")
print(f"   y* = √(2 * {demanda} / {costo_almacenamiento})")
y_optimo = math.sqrt((2 * demanda) / costo_almacenamiento)
y_optimo_redondeado = round(y_optimo, 2)
print(f"   y* = {y_optimo_redondeado}")
