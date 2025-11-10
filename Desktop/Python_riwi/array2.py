# Entrada: [3, 5, 2]
# Salida: La suma total es 10

# lista =[]
# cantidad = int(input("defineme un rango de numeros "))
# for i in range(cantidad):
#     numero = int(input("digite los numeros que quiera guardar"))

#     lista.append(numero)
#     suma = 0
#     for num in lista :
#         suma = suma + num
# print(f"la suma de la lista {lista} es un total de {suma}")


# Entrada: [1, 2, 3, 4]
# Salida: [4, 3, 2, 1]
# esperamos que nos devuelva la misma lista ordenda de diferente manera

# lista1 = []

# while True:
#     numeros = int(input("Agrega numero a la lista (Pon el numero 0 para guardar )"))
#     if numeros == 0 :
#         break
#     elif numeros <= 0 :
#         print("error")
#     lista1.append(numeros)
    
    
# lista1.reverse()
# print(lista1)




# Descripción:
# Dada una lista con números repetidos, crea una nueva lista sin duplicados.
# Ejemplo:
# # Entrada: [1, 2, 2, 3, 4, 4, 5]
# # Salida: [1, 2, 3, 4, 5]
# 👉 Pistas: usa set(lista) o recorre la lista y verifica si el elemento ya está en la nueva lista.

lisori =[]
lisrepet = []
print("te")
print("los numeros repetidos se guardaran en otra lista de repetidos")

while True:
    numeros = int(input("Digitame los numeros que agregaremos a la lista (Oprime 0 para guardar)"))
    if numeros == 0:
        #Rompemos el ciclo while si escriben un 0
        break
    if numeros in lisori and numeros not in lisrepet:

#EXPLICACION

        #estmos diciendo que si numero no se encuentra en lisori y no esta en lisrepeat que lo guarde en repeaat
        #esta manera se entiende mas
        # if numeros in lisori:
        # if numeros not in lisrepet:
        # lisrepet.append(numeros)
        # else:
        # lisori.append(numeros)

        lisrepet.append(numeros)
    else:
        lisori.append(numeros)
        
print("esta es la lista original", lisori)
print("esto son los valores repetidos", lisrepet)

