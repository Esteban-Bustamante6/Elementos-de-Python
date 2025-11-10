# 6. Parqueadero “RapidCar” — Tarifa escalonada
# Tarifa:

# 0 a 5 horas: $2.000 x hora
# 5 horas: $2.000 x hora + multa fija de $5.000

# Validar horas:

# No permitir números negativos.
# Mostrar valor total.

hora = 2000
multa = 5000

Horallegada = int (input("Digita hora de llegada hora militar "))
Horasalida = int (input ( "Digita hora de salida hora militar "))
resta = Horasalida - Horallegada
print(resta)

if resta > 0 and resta < 5:
    total = resta * hora    
    print ("tu valor es ", total)
