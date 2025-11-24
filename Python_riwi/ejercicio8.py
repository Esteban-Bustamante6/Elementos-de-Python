
# nota = ("0.0-5.0")

# calculo nota_final = (tecnica *0.7) + (logica *0.3)

# prueba tecnica 70%
# prueba lógica 30%

# condiciones:
# nota_final >=3 "aprobado"
#         2 =< nota_final <3 "revision"
#          < 2 "reprobado"


print   ("ingrese su nota entre los rangos 0.0-5.0")

nota_tecnica = float (input("coloca la nota que saco en preuba tecnica"))

nota_logica= float (input ("coloca la nota que saco en preuba logica"))


notafinal=(nota_tecnica * 0.70) + (nota_logica * 0.30)



if notafinal >= 3 :
    print ("aprobado su nota es", notafinal)

elif notafinal >= 2  and notafinal <3 :
    print ("revisión su nota es ", notafinal)

elif notafinal < 2 :
    print ("reprobado su nota es", notafinal)

