# CLub "Noche Estelar - Acceso+ validaci+on documento"

# pedir edad

# reglas 

# edad >= 18 = "puede entrar solo si tiene docuemnto"
# si la edad < 18 "Entrada denegada"

# si tiene  18  o mas pero no tiene docuento "debe presentar docuemnto"


Edad  = int (input("ingrese su edad"))

if Edad >= 18 :

    print ("puede entrar solo si tiene docuemnto")  
    Documento = input ("documento en mano si no")
    if Documento == "si" : 
        print ("muestre su documento")
        
    else :     
        print ("como no tienes docuemto no puedes ingresar")
  
elif Edad < 18 and Edad > 0: 
    print ("Entrada denegada")

else  :
    print ("valor errado")


    

