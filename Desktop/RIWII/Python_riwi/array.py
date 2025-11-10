lista = []

while True:
    numero = int(input("Digite varios número (0 para guardar y salir): "))
    if numero == 0:
        
        break
    lista.append(numero)

print("Lista final:", lista)

if len(lista) >= 3 :
    mayor = max(lista)
    menor = min(lista)
    sumarestante = 0
    for num in lista :
        if num != mayor and num != menor :
            sumarestante = sumarestante + num
            
            
else:
    print("Debes ingresar al menos 3 números para hacer la operación.")
print("Número mayor:", mayor)
print("Número menor:", menor)
print("Suma de los demás:", sumarestante)

