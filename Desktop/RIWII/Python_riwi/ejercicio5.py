# 5. Librería “El Saber” — Descuento estudiante + cupón
# Libro cuesta $25.000.

# Si es estudiante → 15% descuento
# Si además tiene cupón "LIBRO10" → 10% adicional sobre el valor ya descontado
# Validar:

# Si no es estudiante, el cupón no aplica.
# Si ingresa cupón incorrecto, ignorarlo.
# Mostrar total.

valor_libro = 25000

print ("bienvenidos a la libreria")
print ("Elije una de las dos opciones")
print ("opcion 1 persona natural")
print ("opcion 2 estudiante")

option= int (input ("escoge entre las opcion "))
cantidad = int(input("Cuantos libros desea alquilar"))
descuento = valor_libro * cantidad
if option == 2 : 
    total = descuento - (descuento * 0.15)
    print ("como eres estuduiante el libro le queda en $", total)

elif option == 1 :
    cupon = input ("Dijite el cupon")
    if cupon == "LIBRO10" : 
        total = descuento - (descuento * 0.10)
        
        print ("Valor del Libro con Cupon es $", total) 
    else :
        print ("cupon incorrecto")



    