from ServicioU3 import agregarProducto,eliminar,estadisticas,exportarCSV,cargarCSV,guardarJSON
from ServicioU3 import actualizar,leer,cargarJSON,cargarCSV,cargarJSON_en_lista
from ServicioU3 import Lista_Inventario
import time

# ! -------- Funcion Menu ---------------!
def menu():
    while True:
        try:
            #mennu principal con el \ n hace un salto de linea en terminal
            opcion = int(input(f'!------------------ Menu Principal ------------------!\n1.Registrar Producto\n2.Eliminar Producto\n3.Actualizar Producto\n4.Mostrar Producto\n5.Exportar a csv\n6.Cargar a JSon \n 7.Cargar a CSV \n8. Estadisticas de inventario \n9. Salir\nOpcion: '))

            if(opcion == 1):
                agregarProducto()
            elif(opcion == 2):
                eliminar(Lista_Inventario)
            elif(opcion == 3):
                actualizar(Lista_Inventario)
            elif(opcion == 4):
                leer(Lista_Inventario)
            elif(opcion == 5):
                exportarCSV()
            elif opcion == 6:
                guardarJSON()
                cargarJSON()
                cargarJSON_en_lista()

            elif opcion == 7:
                Lista_Inventario.extend(cargarCSV())
                guardarJSON()

            elif opcion == 8:
                estadisticas(Lista_Inventario)

            # se hace un conteo regresivo con time para cerrar el programa
            elif opcion == 9:
                print()
                for tiempo in range(3, 0, -1):
                    print(f"Cerrando el programa en: {tiempo}...")
                    time.sleep(1)
                print("[AVISO]: El programa se cerró.")
                break
            else:
                print("[ERROR]: Seleccione una opción válida del (1 al 5).")
        except ValueError:
            print('Mensaje de error')
            continue

print(Lista_Inventario)
#cargan los diccionario a json
total_estudiantes = cargarJSON()
menu()