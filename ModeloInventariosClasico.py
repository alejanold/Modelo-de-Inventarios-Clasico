# Modelo de Inventarios EOQ Clásico
# Autor: Ale Ortiz

import math

print("==== Modelo de inventarios EOQ Clasico ====\n")

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

# Parte 2: Duración del ciclo (t°)
# Fórmula: t° = y* / D
# Esta parte muestra cuánto dura cada ciclo del inventario
print("\n2) Cálculo de la duración del ciclo (t°)")
print(f"   t° = {y_optimo_redondeado} / {demanda}")
t_ciclo = y_optimo / demanda
t_ciclo_redondeado = round(t_ciclo, 4)
print(f"   t° = {t_ciclo_redondeado} días")

# Parte 3: Entero mas grande (n = L / t°)
# Complementando el anterior este nos servira para determinar los ciclos que puede haber en el tiempo de entrega (muy extenso lo sé)
print("\n3) Cálculo del entero más grande (n = L / t°)")
print(f"   n = {dias_entrega} / {t_ciclo_redondeado}")
n = int(dias_entrega / t_ciclo)
print(f"   n = {n}")

# Parte 4: Punto de reorden (Le)
# Fórmula: Le = L - (L / t°)
# Aquí pues, sabremos cada cuantos dias o tal vez ninguno hay que hacer un pedido
print("\n4) Cálculo del punto de reorden (Le)")
print(f"   Le = {dias_entrega} - ({dias_entrega} / {t_ciclo_redondeado})")
Le = dias_entrega - (dias_entrega / t_ciclo)
Le_redondeado = round(Le, 2)
print(f"   Le = {Le_redondeado}")

# Parte 5: Segundo punto de reorden (Le * D)
# Este será el complemento de la parte anterior, porque tambien debemos saber la cantidad de inventario que debemos pedir
print("\n5) Cálculo del segundo punto de reorden (Le * D)")
print(f"   Le * D = {Le_redondeado} * {demanda}")
punto_reorden = Le * demanda
punto_reorden_redondeado = round(punto_reorden, 2)
print(f"   Le * D = {punto_reorden_redondeado}")

# Parte 6 Costo total del inventario (TCU)
# Fórmula: TCU = (K / y* * D) + (h * (y* / 2))
# En esta parte consideramos los pedidos y almacenamiento para sacar un total
print("\n6) Cálculo del costo total del inventario (TCU)")
print(f"   TCU = ({costo_pedido} / {y_optimo_redondeado} * {demanda}) + ({costo_almacenamiento} * ({y_optimo_redondeado} / 2))")
TCU = (costo_pedido / y_optimo * demanda) + (costo_almacenamiento * (y_optimo / 2))
TCU_redondeado = round(TCU, 2)
print(f"   TCU = ${TCU_redondeado}")
