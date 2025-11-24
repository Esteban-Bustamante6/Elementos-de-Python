
# cada producto cuesta $2000

# regla
# 30 unidades 15% descuento
# 10 unidades  5% descuento

# si el total despues del descuento es < $50.000 agregar 5.000 de EnvironmentError

# calcular total final


producto = 2000

Des30= 0.15
Des10= 0.05



Productos= int (input("cuantos productos va  a llevar"))

if Productos >= 30 :
    descuento = producto * Productos
    total =descuento- (descuento*Des30)

    print ("valor a pagar", total)

    if total >= 50000 :
        total = total + 5000

        print ("valor con envio",total)

elif Productos >= 10 and Productos < 29:
    descuento = producto * Productos
    total =descuento- (descuento*Des10)

    print ("valor a pagar", total)

    if total >= 50000 :
        total = total + 5000

        print ("valor con envio",total)



elif Productos < 10 and Productos > 0:
    descuento = producto * Productos
    
    print (" valor totala pagar ", descuento)

else : print ("error")

