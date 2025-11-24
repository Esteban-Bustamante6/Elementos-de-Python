# La panadería de Don Pancho vende pan a $300 cada uno.

# Reglas:

# Si compra más de 20 panes → 10% descuento
# Si compra más de 50 panes → 20% descuento
# Si ingresa una cantidad negativa, mostrar "Cantidad inválida"
# Calcular y mostrar el total.


print("bienvenido al local de don pacho")
cantidad = int(input("cuantos panes desea comprar"))
precio = 300
total = precio * cantidad
if cantidad >= 20 and cantidad <=49:
    print(f"tenemos un descneto del 10% por la compra de {cantidad} panes")
    
    totaldes = total -(total *0.10)
    print(f"su cantidad a pagar es de {totaldes}")
elif cantidad >= 50:
    print(f"tenemos un descneto del 20% por la compra de {cantidad} panes")
    porcentaje = (precio * 0.20) * cantidad
    totaldes = total -(total *0.20)

    print(f"su cantidad a pagar es de {totaldes}")
elif cantidad <=19 and cantidad >=1:

    print("Deberas a pagar 300")

else : 
    print("Cantidad inalidad fuera de la tienda")