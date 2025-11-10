# Heladería “Frosty” — Sabor y topping
# Sabores y precios:

# chocolate → $4.000
# vainilla → $3.500
# Opcional: topping cuesta $1.000.

# Si el usuario ingresa un sabor que no existe, mostrar "Sabor no disponible".
# Si el sabor es válido, preguntar si quiere topping y calcular total.


chocolate = 4.000
vainilla = 3.500
topping = 1.000

sabor = input ("sabor del helado  ")

if sabor == "chocolate" :
    Toppings = int (input ("cuantos topings dese agregar"))

    print ("sabor a chocolate 4.000")
    precio = topping * Toppings
    print (f"tu escogiste {Toppings} toppins    ahora tu valo a pagar es de {precio + 4.000}")

elif sabor == "vainilla":
    Toppings = int (input ("cuantos topings desea agregar"))

    print ("sabor a vainilla 3.500")
    precio = topping * Toppings
    print (f"tu escogiste {Toppings} toppins    ahora tu valo a pagar es de {precio + 3.500}")

else : 
    print ("Sabor no disponible")
