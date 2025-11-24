# crearemos un programa de registro de un producto hacia un inventario de una tienda donde agregaremos el precio y la cantidad , un usuario escogera un producto con su cantidad que desee llevar y devolveremos el costo final que debe de pagar el usuario


#iniciamos con un mensaje  de bienvenida
print("bienvenido a la tienda ELMASGUE")

# preguntaremos que producto es el seleccionado y lo guardaremos en producto
producto = input("Escribe el producto que deseas llevar  :")

#haremos un ciclo while para controlar errores y que me pregunte de nuevo
# decimos que mientras halla algo el producto se ejecute 
while producto:
    #preguntamos la cantidad de dicho producto
    cantidad = int(input(f"cual es la cantidad que deseas llevar de {producto}  :"))
    # si la cantidad es 0 o negativa pregunte de nuevo la cantidad
    if cantidad <= 0 :
        continue
    #si es superio a 0 entonces preguntara el precio que vio
    elif cantidad > 0 :
        precio = float(input("Cual fue el precio que vio en el stante  :"))
        # si el precio es 0 o negativo vuelve a preguntar la cantidad 
        if precio <= 0.0 :
            print("Eror precio invalido")
            continue
        # si es mayor a 0 me multiplicara precio * cantidad y guardara en precioTotal
        else:
            precioTotal = precio * cantidad
            #rompe el ciclo para que no pregunte mas
        break

#mostramos de manera organizada todo la informacion de producto
print(f"Prodcuto= {producto} / precioUND= {precio} / Cantidad= {cantidad} / Total= {precioTotal}")

