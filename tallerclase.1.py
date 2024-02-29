import os
os.system('cls')
var_cantidad_numeros = int(input('Ingresa la cantidad de números a evaluar: '))

var_numeros_en_rango = 0
var_contador = 0



while var_contador < var_cantidad_numeros:
    numero = float(input('Ingresa un número: '))
    
    if 10<= numero <= 20:
        var_numeros_en_rango += 1
    
    var_contador += 1

print(f"\nCantidad de números en el rango de 10-20: {var_numeros_en_rango}")