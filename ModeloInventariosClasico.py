# Modelo de Inventarios EOQ Clásico + Inventarios con descuento
# Autor: Ale Ortiz

import math

print("- Modelo de inventarios EOQ Clasico -\n")

# Aquí pediré los datos para aplicar el modelo
costo_pedido = float(input("Ingresa el costo de pedido (K): "))
demanda = float(input("Ingresa la demanda del producto (D): "))
costo_almacenamiento = float(input("Ingresa el costo de almacenamiento y proceso (h): "))
dias_entrega = float(input("Ingrese en cuántos días recibes tu pedido (L): "))

print("\n- Aqui va el paso a paso -")

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

# Parte final: En conclusión
# Pues ya estaria, aqui como en clase solo dare un enunciado sencillo indicando cada cuantos dias o a partir de que cantidad hacer un pedido
print("\n=== En conclusión ===")
print(f"Se deben pedir {y_optimo_redondeado} cantidad cada {Le_redondeado} días "
      f"o cada que el inventario caiga a {punto_reorden_redondeado} unidades.")
print(f"\nCosto total del inventario (TCU): ${TCU_redondeado}")

#   Parte sorpresa: INVENTARIOS CON DESCUENTO
# Segun yo aqui es revisar cada nivel y ver cuál conviene más.

print("\n==== Modelo de inventarios con descuento ====\n")

# Aquí se va a pedir cuántos niveles maneja el proveedor
niveles = int(input("Ingrese cuántos niveles de descuento ofrece el proveedor: "))

# Guardo los precios y las cantidades
precios = []
cantidades_min = []

# Aqui me confundi, porque se debe pedir la informacion de precio y cantidad mínima jaja
for i in range(niveles):
    print(f"\nNivel {i+1}:")
    precio = float(input("  Ingrese el precio por unidad en este nivel: "))
    cantidad_min = float(input("  Cantidad mínima para obtener este precio: "))
    precios.append(precio)
    cantidades_min.append(cantidad_min)
print("\n- Calculando cada nivel -")

# Estas variables nos sirven para quedarnos con la mejor opción
mejor_TCU = None
mejor_Q = None
mejor_precio = None
for i in range(niveles):
    print(f"\n>>> Nivel {i+1} (precio = {precios[i]}, mínimo = {cantidades_min[i]})")

    # En este parte, el costo de almacenamiento depende del precio por unidad
    h_nivel = 0.25 * precios[i]

    # El EOQ aqui, se recalcula usando el costo de almacenamiento
    Q_nivel = math.sqrt((2 * demanda * costo_pedido) / h_nivel)
    Q_red = round(Q_nivel, 2)

    print(f"  EOQ nivel {i+1}: Q = √((2 * {demanda} * {costo_pedido}) / {h_nivel}) = {Q_red}")

    # y aqui si el EOQ no alcanza la cantidad mínima que nos pide el proveedor, se tiene que ajustar
    if Q_nivel < cantidades_min[i]:
        print(f"  Q calculado NO alcanza el mínimo. Se ajusta a {cantidades_min[i]}")
        Q_nivel = cantidades_min[i]

    # para que no se me olvide sobre el costo de inventario:
    # (D/Q)*K: costo de realizar pedidos
    # h*(Q/2): costo de mantener inventario
    # D*precio: costo de comprar el producto
    TCU_nivel = (demanda / Q_nivel) * costo_pedido + (h_nivel * (Q_nivel / 2)) + (demanda * precios[i])
    TCU_red = round(TCU_nivel, 2)
    print(f"  TCU nivel {i+1}: {TCU_red}")

# DEspues de eso, aqui se entra en una tipo revision para corroborar resultados y saber si es el mejor
    if mejor_TCU is None or TCU_nivel < mejor_TCU:
        mejor_TCU = TCU_nivel
        mejor_Q = Q_nivel
        mejor_precio = precios[i]

# ya haciendo las operaciones con todos los niveles, aqui se muestra cuál puede convenir más
print("\n- Resultado final -")
print(f"El mejor nivel es con precio ${mejor_precio}")
print(f"Cantidad a pedir (Q): {round(mejor_Q, 2)} unidades")
print(f"Costo total mínimo: ${round(mejor_TCU, 2)}")

# Por fin aqui se hace la interpretacion y se lanzan los resultados finales
print("\nConclusión:")
print(f"Conviene comprar al precio ${mejor_precio}, pidiendo {round(mejor_Q, 2)} unidades,")
print("porque ese nivel da el costo total más bajo considerando el almacenamiento,")
print("los pedidos y el precio que cobrara el proveedor.")
