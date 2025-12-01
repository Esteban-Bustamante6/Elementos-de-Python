import csv

ARCHIVO_CSV = r"C:\Users\Administrador\Desktop\RIWII\Modle_Riwi\Membership\Usuario.csv"

User = []

#------------------------------- init cvs-----------------------------------------------
def User_Create_Auto():
    rol = "Admin"
    Password = 1324
    UserDic = {
        "Rol" : rol,
        "Password": Password
    }
    User.append(UserDic)
    return User

def Load_User_Csv():
    with open(ARCHIVO_CSV, "w", newline="") as archivo:
        write = csv.writer(archivo)
        write.writerow(["Rol" , "Password"])
        for u in User:
            write.writerow([u["Rol"], u["Password"]])

    print("\n[OK] Datos exportados a Usuario.csv\n")

def cargarCSV():
    datos = []
    try:
        with open(ARCHIVO_CSV, "r", encoding="latin-1") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                datos.append({
                    "Rol": fila["Rol"],
                    "Password": int(fila["Password"])
                })

        print("\n[OK] Datos cargados desde Usuario.csv\n")

    except FileNotFoundError:
        print("\n[ADVERTENCIA] No existe Usuario.csv aún.\n")

    return datos
#-------------------------------- finish cvs-----------------------------------------

def Validacion():
    usuarios = User_Create_Auto() # Traemos los datos del csv
    inten = 3

    while inten >= 0:
        name = str(input("Put at Username for login "))
        if name.isalpha():
            print("ok")
        else:
            print("Date invalid ")
        try:
            contra = int(input("Put de password of Username"))
            if contra <= 0 :
                print("Date negative")
        except ValueError:
            print("Error number")
            inten -= 1

        acceso = False
        for u in usuarios:
            if name == u["Rol"] and contra == u["Password"]:
                acceso = True
                break
        
        if acceso:
            print(f"Acceso consedido usuario {name}")
        else :
            inten -= 1
            print(f"you have exhausted yourself at intent ... intent restant = {inten}")

    