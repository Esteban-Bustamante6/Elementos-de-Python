
# Iniciamos declarando una lista vacia y un contador
listaInventario = []

conteo = 0
# repetiremos un mennu interactivo X veces o hasta que pongan fin
while True:
    print("Esto es un MENÚ INTERACTIVO  .")
    print("(1). Agregar Producto")
    print("(2). Mostrar inventario")
    print("(3). Calcular estadística")
    print("Escriba FIN para salir")

    
    opcion = input("Elige una opción: ")
    # pasamos la opcion a toda minuscula con .lower y validamos si puso fin
    if opcion.lower() == "fin":
        break #rompe el while
    
    # si en vez de fin puso un "numero" lo pasamos a flotante
    opcion = float(opcion)

    # OPCIÓN 1 - AGREGAR PRODUCTO
    if opcion == 1:
        # creamos un diccionario con unas claves especificas y le pedimos el valor al usuario por input
        Producto = {
            "Nombre": input("Nombre del producto: "),
            "Cantidad": int(input("Cantidad: ")),
            "Precio": float(input("Precio: "))
        }

        #Agregamos dichos productos a una listaInventario
        listaInventario.append(Producto)

        #a conteo que inicialmente estaba en cero le sumamos 1 cada vez que se realice un registro de producto
        conteo += 1

    # OPCIÓN 2 - MOSTRAR INVENTARIO
    if opcion == 2:

        #validamos con len() que si listaInventario tiene algun valor
        #Len() cuenta cuantos valores tiene por dentro una lista
        if len(listaInventario) == 0:

            #si no tiene ningun valor es por que etsa vacia
            print("Inventario vacío, agrega productos primero.")
        else:
            print("INVENTARIO ACTUAL:")
            
            #declaramos un for que recorra la listaInventario
            for prod in listaInventario:

                #Me muestra los valores o en este caso los prod = Productos de la lista
                print(prod)


    # OPCIÓN 3 - CALCULAR VALOR TOTAL DEL INVENTARIO
    if opcion == 3:
        if len(listaInventario) == 0:
            print("No hay productos para calcular estadísticas.")
        else:
            total_inventario = 0

            # declaramos otro for para que me recorra la lista
            for i in listaInventario:
                #en este for le indicaremos que queremos dicha posicion de cada producto por medio de []
                total_inventario += i["Precio"] * i["Cantidad"]

            #esto nos traer los precio y cantidad de cada producto y los multiplicara y seran mostrados su resultado mediante este print
            print(f"Valor total del inventario: {total_inventario} y la cantidad de productos final son de {conteo}")

