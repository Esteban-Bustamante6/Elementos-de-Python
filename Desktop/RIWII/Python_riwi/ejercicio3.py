# Pedir cuántos días entrenó esta semana.

# ≥ 4 días → "¡Excelente disciplina!" + gana 1 punto de energía
# 2 o 3 → "Bien, pero puedes dar más"
# 0 o 1 → "No aflojes, tú puedes mejorar"
# Mostrar mensaje y si aplica, los puntos ganados.

print("bienvenido al gym solo leveling")
dias = int(input("me das a digitar la cantidad de dias que entrenas por semana"))

if dias >= 4 :
    print("Tienes una excelente disciplina ")
    print(" haz ganado 1 Punto")
elif dias >= 2 and dias <=3 :
    print("Bien, pero podes dar mucho mas")
    print(" No tienes  Punto")

else :
    print("No afloje, tu puedes mejorar muhcoo")
    print(" No tienes  Punto")
