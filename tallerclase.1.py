import os
os.system('cls')
var_cantidad_numeros = int(input('Ingresa la cantidad de números a evaluar: '))

var_numeros_en_rango = 0
var_contador = 0



while var_contador < var_cantidad_numeros:
    numero = float(input('Ingresa un número: '))
    
    if numero >= 10 and numero <= 20:
        var_numeros_en_rango += 1
    
    var_contador += 1

print('\nCantidad de números en el rango de 10-20:', var_numeros_en_rango)
