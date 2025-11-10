# 2. Encontrar números primos en una lista

# Descripción:
# Pide al usuario varios números.
# Devuelve una lista con los números que son primos (solo divisibles por 1 y por sí mismos).
# Ejemplo:
# Entrada: [2, 4, 5, 6, 7]
# Salida: [2, 5, 7]

# lis = []
# lisi =[]
# while True:
#     numb = int(input("Digita los numeros de la lista  (OPRIME 0 PARA GUARDAR )"))
#     if  numb == 0 :
#         break
#     if numb % 2 == 0 :
#         lis.append(numb)
#     else:
#         lisi.append(numb)
# print("la lista con los numeros pares es ",lis)
# print("la lista con numeros impar es", lisi)





# 2. Eliminar los valores repetidos de una lista

# Descripción:
# Pide al usuario que ingrese varios números y genera una nueva lista sin duplicados.
# Ejemplo:
# Entrada: [2, 4, 2, 6, 4, 7]
# Salida: [2, 4, 6, 7]
# Pista: Usa if elemento not in nueva_lista: antes de hacer .append().
lisi =[]
lis = []

while True:
    numb = int(input("Digita los numeros de la lista  (OPRIME 0 PARA GUARDAR )"))
    if  numb == 0 :
        break
    if numb in lis and numb not in lisi:
        lisi.append(numb)
    
    else :
        lis.append(numb)
print("lista principal", lis)
print("lista con numero eliminado",lisi)
print('sapo tupis ')