# . Suma de números pares en una lista
# Objetivo: Leer varios números, guardarlos en una lista y mostrar la suma de los números pares.
# Ejemplo:
# Entrada → [2, 5, 8, 3, 10]
# Salida → La suma de los pares es: 20
# Pistas:
# Usa input() dentro de un bucle while o for.
# Usa if num % 2 == 0: para verificar si es par.
# Guarda los números en una lista y usa sum().

lisorigi = []

while True:
    numero = int(input("Digite numero (OPRIMA 0 PARA GUARDAR)"))

    if numero == 0 :
        break
    lisorigi.append(numero)
    list2 = []
    for num in lisorigi :
        if num % 2 ==0 :
            list2.append(num)
print(f" lista original {lisorigi}  y list2 {list2}")
print(sum(list2))