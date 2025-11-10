# El usuario ingresa dos notas (0.0 - 5.0):

# Prueba técnica (70%)
# Prueba lógica (30%)
# Cálculo: nota_final = (tecnica * 0.7) + (logica * 0.3)

# Condiciones:

# nota_final ≥ 3 → “Aprobado”
# 2 ≤ nota_final < 3 → “Revisión”
# < 2 → “Reprobado”
# Validar que las notas estén en rango.

tecnica = 0.70
logica = 0.30

notaTe = float(input("Por favor digite la nota que saco en la prueba Tenica, en un rango de 0.0 a 5.0 "))
notaLo = float(input("Por favor digite la nota que saco en la prueba logica, en un rango de 0.0 a 5.0 "))


notaFinal = (notaTe * tecnica) + (notaLo * logica) 

if notaFinal >= 3 :
    print("Aprobado")
elif notaFinal >= 2 and notaFinal <3 :
    print("Revision")
elif notaFinal < 2 and notaFinal > 0 :
    print("Repobado")
else: 
    print("A no mijo a qu vino")