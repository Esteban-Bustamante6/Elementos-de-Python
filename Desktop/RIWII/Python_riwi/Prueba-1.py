#Primer tarea , necesito que hagan un código que recorra un número de 0 a la cantidad de veces que se pida por terminal Y imprimir en pantalla si la posición es par o impar

rango = int(input("Digite un numero que se convertira en el rango de la operacion"))

for i in range(rango):
    i = i +1
    if i % 2 == 0 :
        print("este numero es par =", i)
    else : 
        print("estos numero son impares =", i)




#Segundo ejercicio necesito un código que pase los números de decimal a binarios

decimal = int(input("Digite un numero decimal que quieras convertir a binarios"))
binario = ""
while (decimal > 0 ):
    residuo = decimal % 2
    decimal = decimal // 2 
    binario = str(residuo ) + binario
    print(f'el numero digitado en codigo binario seria el {binario}')