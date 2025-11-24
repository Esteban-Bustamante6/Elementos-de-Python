import csv

ARCHIVO_CSV = r"C:\Users\Administrador\Desktop\RIWII\Modle_Riwi\simuacro\Usuario.csv"
usuario = []

# CREA EL USUARIO POR DEFECTO
def validacionUsuario():
    Rol = "Administrador"
    contraseña = 1324
    usuarioDic = {
        "Rol": Rol,
        "Contraseña": contraseña
    }
    usuario.append(usuarioDic)

# EXPORTA AL CSV
def exportarCSV():
    with open(ARCHIVO_CSV, "w", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["Rol", "Contraseña"])  # encabezados
        for u in usuario:
            writer.writerow([u["Rol"], u["Contraseña"]])

    print("\n[OK] Datos exportados a Usuario.csv\n")

# CARGA EL CSV Y RETORNA UNA LISTA DE DICCIONARIOS
def cargarCSV():
    datos = []
    try:
        with open(ARCHIVO_CSV, "r", encoding="latin-1") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                datos.append({
                    "Rol": fila["Rol"],
                    "Contraseña": int(fila["Contraseña"])
                })

        print("\n[OK] Datos cargados desde Usuario.csv\n")

    except FileNotFoundError:
        print("\n[ADVERTENCIA] No existe Usuario.csv aún.\n")

    return datos

# LOGIN USUARIO
def login_Usuario():
    datos = cargarCSV()  # ← AQUÍ cargamos los usuarios

    usuario_input = input("Digite su usuario para iniciar sesión: ")
    intentos = 3

    while intentos > 0:
        try:
            contraseña_input = int(input("Ponga la contraseña del usuario: "))
        except ValueError:
            print("La contraseña debe ser numérica.")
            intentos -= 1
            continue

        # Validación de usuario/contraseña
        acceso = False
        for u in datos:
            if u["Rol"] == usuario_input and u["Contraseña"] == contraseña_input:
                acceso = True
                break

        if acceso:
            print("\n✔ Acceso concedido. Bienvenido!")
            return
        else:
            intentos -= 1
            print(f" Contraseña incorrecta. Intentos restantes: {intentos}")

    print("\nAcceso bloqueado. Superó el número de intentos.")

# ---- EJECUCIÓN ----
validacionUsuario()
cargarCSV()
exportarCSV()
login_Usuario()
