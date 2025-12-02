import time
import json
import csv

Lista_Inventario = []

#se asinga el nombre con el que se creara los archivos 
ARCHIVO_JSON = "Inventario.json"
ARCHIVO_CSV = "Inventario.csv"

# ✔ Guardar en JSON
def guardarJSON():
    with open(ARCHIVO_JSON, "w") as archivo:# la "w" es para sobre escribir
        json.dump(Lista_Inventario, archivo, indent=4)
    print("\n[OK] Datos guardados en estudiantes.json\n")

# ✔ Cargar desde JSON
def cargarJSON():
    try:
        with open(ARCHIVO_JSON, "r") as archivo: #la "r" es para leer
            datos = json.load(archivo)
            return datos
    except FileNotFoundError:
        return []   # si no existe, lista vacía
    
def cargarJSON_en_lista():
    #se encarga de validar que la lista es la que este cargando en el json
    global Lista_Inventario
    Lista_Inventario = cargarJSON()
    print("\n[OK] Inventario cargado desde Inventario.json\n")


# ✔ Exportar a CSV
def exportarCSV():
    with open(ARCHIVO_CSV, "a", newline="") as archivo: #la "a" es para agregrar
        writer = csv.writer(archivo)
        writer.writerow(["Nombre", "Cantidad", "Precio"])  # encabezados del archivo
        for prod in Lista_Inventario:
            writer.writerow([prod["Nombre"],prod["Cantidad"],prod["Precio"]])

    print("\n[OK] Datos exportados a Inventario.csv\n")

def cargarCSV():
    datos = []
    try:
        with open(ARCHIVO_CSV, "r") as archivo:
            lector = csv.reader(archivo)
            next(lector)  # saltar encabezado

            for fila in lector: #configuramos como quiremos que se añadan los valores y de donde los vamos a tomar
                if len(fila) == 3:
                    nombre, cantidad, precio = fila
                    datos.append({
                        "Nombre": nombre,
                        "Cantidad": int(cantidad),
                        "Precio": float(precio)
                    })
        print("\n[OK] Datos cargados desde Inventario.csv\n")
    except FileNotFoundError:
        print("\n[ADVERTENCIA] No existe Inventario.csv aún.\n")

    return datos


# * Funcion crear estudiantes
def agregarProducto():
    while True:
        try:
            # ? --- VALIDAR NOMBRE ---
            while True:
                nombre = input('Ingrese el nombre del Producto : ')
                if nombre.isalpha(): #isalpha valida que los caracteres STR vallan de la A a la Z
                    break
                print("[ERROR]: El nombre solo debe contener letras.")

            # ? --- VALIDAR APELLIDO ---
            while True:
                try:
                    cantidad = int(input('Ingrese la cantidad del producto '))
                    if cantidad <= 0:
                        print("[ERROR]: cantidad invalido.")
                        continue
                    else:
                        break
                except ValueError:
                    print('[ERROR]: Valores no válidos, ingrese nuevamente los datos.\n')


            while True:
                try:
                    precio = float(input('Ingrese el precio del producto '))
                    if precio <= 0:
                        print("[ERROR]: precio invalido.")
                        continue
                    else:
                        break
                except ValueError:
                    print('[ERROR]: Valores no válidos, ingrese nuevamente los datos.\n')

            Producto = {
                'Nombre': nombre,
                'Cantidad': cantidad,
                'Precio' : precio }
            # se añade diccionario
            Lista_Inventario.append(Producto)
            
            print("\nProducto agregado:", Producto)

            while True:
                salir = input('Desea agregar otro Producto? (s/n): ')
                if salir.lower() == "s":
                    print(f'\nTotal de Producto: {Lista_Inventario}')
                    break
                elif salir.lower() == "n":
                    return

        except ValueError:
            print('[ERROR]: Valores no válidos, ingrese nuevamente los datos.\n')

# * Funcion eliminar
def eliminar(Producto):
    if not Producto:
        print("No hay productos para eliminar.")
        return

    try:
        Nombre_buscar = input("Ingrese el Nombre del producto a eliminar: ")
    except ValueError:
        print("Debe ingresar un Nombre existente.")
        return

    encontrado = False
    for prod in Producto:
        if prod["Nombre"] == Nombre_buscar:
            encontrado = True
            print(f"Producto encontrado: {prod}")

            confirmacion = input("¿Está seguro que desea eliminarlo? (s/n): ")

            if confirmacion.lower() == 's':
                Producto.remove(prod)
                
                print("Producto eliminado correctamente.")
            else:
                print(" Operación cancelada.")
            break

    if not encontrado:
        print("No existe un Producto con ese Nombre.")

# * Funcion Actualizar
def actualizar(Producto):
    if not Producto:
        print("No hay Productos para actualizar.")
        return

    name_buscar = input("Ingrese el Nombre del producto a actualizar: ")

    encontrado = False
    for prod in Producto:
        if prod["Nombre"] == name_buscar:
            encontrado = True
            print(f"Estudiante encontrado: {prod}")

            # Nuevos datos
            nombre = input("Ingrese el nuevo nombre: ")
            precio = float(input("Digite el precio del Producto"))
            cantidad = int(input("Digite la cantidad que va a lllevar"))
            #decimos que en el prod con la clave del diccionario añadiremos un nuevo valor
            prod["Nombre"] = nombre
            prod["Cantidad"] = cantidad
            prod["Precio"] = precio

            print("\nProducto actualizado correctamente:")
            print(prod)
            
            break

    if not encontrado:
        print("[ERROR]: No existe un producto")


# * Funcion mostrar valores
def leer(Producto):
    if not Producto:
        print("No hay información")
    else:
        print("\n----- Lista de producto -----")
        for prod in Producto:
            print(f"nombre: {prod['Nombre']}, Cantindad: {prod['Cantidad']}, Precio: {prod['Precio']}")
        print("--------------------------------\n")

# !-------- Funcion Estadisticas ------------!
def estadisticas(Producto):
    if not Producto:
        print("\n[ADVERTENCIA] No hay productos en el inventario.\n")
        return
    #sumamos todas las cantidades y precio de producto con un for
    unidades_totales = sum(prod["Cantidad"] for prod in Producto)
    valor_total = sum(prod["Cantidad"] * prod["Precio"] for prod in Producto)
    #Indica cómo seleccionar el valor que se comparará. y lambda es Indica que, para cada producto, use su "Cantidad" para comparar
    producto_mas_caro = max(Producto, key=lambda p: p["Precio"])
    producto_mayor_stock = max(Producto, key=lambda p: p["Cantidad"])

    print("\n────────── ESTADÍSTICAS DEL INVENTARIO ──────────")
    print(f"Unidades totales: {unidades_totales}")
    print(f"Valor total del inventario: ${valor_total:,.2f}")
    print(f"Producto más caro: {producto_mas_caro['Nombre']} (${producto_mas_caro['Precio']})")
    print(f" Producto con mayor stock: {producto_mayor_stock['Nombre']} ({producto_mayor_stock['Cantidad']} unidades)")
    print("──────────────────────────────────────────────────\n")

