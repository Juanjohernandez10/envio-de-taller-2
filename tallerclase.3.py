import os
os.system('cls')

while True:
    os.system('cls')
    print("1. Realizar compra")
    print("2. Realizar venta")
    print("3. Mostrar inventario")
    print("4. Salir")

    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        var_codigo = input("Ingrese el código del producto: ")
        var_nombre = input("Ingrese el nombre del producto: ")
        var_existencias = int(input("Ingrese la cantidad de productos a comprar: "))
        var_precio_unitario = float(input("Ingrese el precio unitario del producto: "))
        var_inventario = (input('inventario'))

        if var_codigo in var_inventario : 
           var_inventario[var_codigo]["existencias"] += var_existencias
        else:
            nuevo_producto = {"nombre": var_nombre, "existencias": var_existencias, "precio_unitario": var_precio_unitario}
            var_inventario[var_codigo] = nuevo_producto

        print("Compra realizada con éxito.\n")

    if opcion == "2":
        var_codigo = input("Ingrese el código del producto: ")

        if var_codigo in var_inventario:
            cantidad_a_vender = int(input(f"Ingrese la cantidad de 'inventario[var_codigo] a vender: "))

            if cantidad_a_vender > var_inventario[var_codigo]["existencias"]:
                print("Error: No hay suficientes existencias para realizar la venta.")
            else:
                var_inventario[var_codigo]["existencias"] -= cantidad_a_vender
                print("Venta realizada con éxito.")
        else:
            print("Error: Producto no encontrado en el inventario.\n")

    if opcion == "3":
        print("Inventario actual:\n")
        for codigo, producto in var_inventario.items():
            print(f"Código: {var_codigo}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Existencias: {producto['existencias']}")
            print(f"Precio Unitario: ${producto['precio_unitario']}\n")

    if opcion == "4":
        print("Saliendo del programa. ¡Hasta luego!")
        break

    if opcion != ["1", "2", "3", "4"]:
        print("Opción no válida. Por favor, seleccione una opción válida.\n")