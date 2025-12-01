
equipos = []
categoria =[]
estado_actual = []
def Registro_Equipos():
    print("vamos a añadir un nuevo equipo al inventario")
    intento = 2
    while True :
        try:
            Nombre_Equipo = input("Digite el nombre del equipo :")
            if Nombre_Equipo.isalpha() :
                equipo = {
                "Nombre": Nombre_Equipo}
                equipos.append(equipo)
                print(equipos)
            else :
                print("solo se permiten caracteres de tipo str")
                

                intento -= 1
                if intento <= 0:
                    break
                continue
        except ValueError:
            print("Solo se permiten caracteres de tipo STR")
        try:
            desea = input("Desea añadir categoria si / no :")
            if desea.lower() ==  "si":

                categoria = str(input("Digite la categoria del equipo\nDrones\nLaptop\nTablet\nCamara\nHerramienta\nObjetos Varios\n Escriba el nombre de la categoria del equipo :"))

                #Nueva manera de agregar a diccionario solamente se necesita poner una clave mediante [] y asignarle un valor
                equipo["Categoria"]= categoria
                print(equipo)
            else:
                

            
        except ValueError:
            print("dato invalido")
        
        
        while True:
                salir = input('Desea agregar otro equipos? (si/no): ')
                if salir.lower() == "si":
                    print(f'\nTotal de Producto: {equipo}')
                    break
                elif salir.lower() == "no":
                    return
Registro_Equipos()
