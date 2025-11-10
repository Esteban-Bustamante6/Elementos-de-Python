# Restaurante “El Sabor Colombiano” — Menú + bebida opcional + IVA
# Menú: $12.000

# Opciones bebida:

# sí → $3.000
# no → $0
# Luego aplicar IVA del 8% al total final.
# Mostrar valor con IVA incluido.



mennu = 12000
bebida = 3000

print("Bienvindo al restaurante")
option = input("tenemos el mennu del dia a un excelente precio, lo desea, Si / NO")

if option == "SI" or option =="si":
    print("el menu del dia tiene una valor de $12.000")
    desea = input("Desea agregar una bebida a su orden : Si/No")
    if desea == "SI" or desea =="si":
        dos = mennu + bebida
        iva = dos * 0.08
        total_iva = dos + iva 

        print(" su total a pagar sera $",total_iva)
    elif desea == "NO" or desea == "no":
        iva = mennu * 0.08
        total_iva = mennu + iva 

        print("el valor total de su orden con bebida es de =$",total_iva)
    else :
        print("No valido")
elif option == "No" or option == "no":
    print("Gracias por venir")
else:
    print("error dato no valido")