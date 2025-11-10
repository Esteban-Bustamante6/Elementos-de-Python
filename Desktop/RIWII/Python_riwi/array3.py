# Separar números pares e impares en listas distintas

# Descripción:
# Crea un programa que lea varios números y los separe en dos listas: una para los pares y otra para los impares.
# Ejemplo:
# # Entrada: [1, 2, 3, 4, 5, 6]
# # Salida:
# # Pares: [2, 4, 6]
# # Impares: [1, 3, 5]
# 👉 Pistas: usa el operador % (módulo) y condicionales if.



# listaPar = []
# listaImpar = []

# while True:
#     numeros = int(input("digita numero  (OPRIME 0 PARA GUARDAR)"))
#     if numeros == 0 :
        
#         break
#     if numeros % 2 == 0 :
#         listaPar.append(numeros)
#     else:
#         listaImpar.append(numeros)
# print("lista de numeros par", listaPar)
# print("lista de numero impar", listaImpar)




# 2.Contar cuántas veces aparece un número en una lista

# Descripción:
# Pide al usuario varios números, guárdalos en una lista y luego solicita un número para contar cuántas veces aparece.
# Ejemplo:
# # Lista: [2, 3, 2, 5, 2, 1]
# # Número a buscar: 2
# # Salida: El número 2 aparece 3 veces.
# 👉 Pista: usa el método .count().

lista = []
while True:
    numb = int(input("Digite numero  (OPRIMA 0 PARA GUARDAR)"))
    if numb == 0:
        break
    lista.append(numb)
bucar = int(input("Digita el numero que desea saber cuantas veces se repite y posicion"))
#. funcion .count ayuda a buscar cuantas veces se repite el parametro que esta en () en la lista seleccionada
print(f"el numero {bucar} aparece {lista.count(bucar)} veces en la lista")

position = []
for i in range(len(lista)):
    if lista[i] == bucar:
        position.append(i +1)
        print(f"Se encontró por primera vez en la posición {position[0]}")
        print(f"Todas las posiciones donde aparece: {position}")


