# 9. Supermercado “AhorroMax” — Descuentos y envío
# Cada producto cuesta $2.000.
# Reglas:
# 30 unidades → 15% descuento
# 10 unidades → 5% descuento
# Si el total después del descuento es < $50.000 → agregar $5.000 de envío
# Calcular total final.

print("bienvenido al Supermercado 'AhorroMax'")
cantidad = int(input("cuantos productos desea comprar"))
precio = 2000
total = precio * cantidad
if cantidad >= 30:
    print(f"tenemos un descneto del 15% por la compra de {cantidad} panes")
    
    totaldes = total -(total *0.15)
    print(f"su cantidad a pagar es de {totaldes}")
elif cantidad <= 29 and cantidad >= 10:
    print(f"tenemos un descneto del 5% por la compra de {cantidad} panes")

    totaldes = total -(total *0.05)

    print(f"su cantidad a pagar es de {totaldes}")
elif cantidad <=9 and cantidad >=1:
    
    print("Deberas a pagar ", total)

else : 
    print("Cantidad inalidad fuera de la tienda")