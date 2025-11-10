

edad = int(input("señor usuario por favor ingrese su edad"))
descuento = -4.000
if edad <= 5 and edad >= 1:
    print("Afortunado entras gratis")
elif edad >5 and edad <=11:
    print(f" su edad es de {edad} años ,, por lo tanto debes de pagar 5.000")
elif edad >11 and edad <=59:
    print(f" su edad es de {edad} años ,, por lo tanto debes de pagar 8.000")
elif edad >=60 :
    descuento = -4.000 + 8.000
    print(f" su edad es de {edad} años ,,, tienes un descuento adicional")
    print("solo deberas de pagar",descuento)
else :
    print("edad invalidad no entras")