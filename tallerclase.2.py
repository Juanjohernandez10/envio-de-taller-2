
import os
os.system('cls')
cons_computador_escritorio = 2000000
cons_tabletas= 3000000
cons_videobeam= 5000000
cons_televisor = 7000000


var_cantidad_computadores_escritorio = 0
var_cantidad_tabletas = 0
var_cantidad_videobeams = 0
var_cantidad_televisiones = 0


var_total_a_pagar = 0

while True:
    os.system('cls')
    print('Seleccione una opción:')
    print('1. Computador de escritorio')
    print('2. Tableta')
    print('3. Videobeam')
    print('4. Televisor')
    print('5. Facturar')
    
    
    opcion = input()

    
    if opcion == "1":
        var_cantidad_computadores_escritorio += 1
        var_total_a_pagar += cons_computador_escritorio
        print("Computador de escritorio añadido al carrito.")
    
    if opcion == "2":
        var_cantidad_tabletas += 1
        var_total_a_pagar += cons_tabletas
        print("tableta añadido al carrito.")
    
    if opcion == "3":
        var_cantidad_videobeams += 1
        var_total_a_pagar += cons_videobeam
        print("videobeam añadida al carrito.")
    
    if opcion == "4":
        var_cantidad_televisiones += 1
        var_total_a_pagar += cons_televisor
        print("televisor añadido al carrito.")
    os.system('cls')
    if opcion == "5":
        break  # mejor sistema para poder cerrar el bucle sin colocar false 
    
    if opcion != ("1", "2", "3", "4", "5", "6"):
        print("Opción no válida. Intente de nuevo.")
        
print(f"\nResumen de la factura:") 
print(f"Computadores de escritorio: {var_cantidad_computadores_escritorio }")
print(f"tabletas: {var_cantidad_tabletas}")
print(f"videobeam: { var_cantidad_videobeams}")
print(f"televisor: {var_cantidad_televisiones}")
print(f"Total a pagar: ${var_total_a_pagar}")        