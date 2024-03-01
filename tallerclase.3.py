import os
os.system('cls')
codigoInt = int(input('codigo'))
nombrestr = input('nombre')
existenciasInt = 0
controlBln = True
os.system('cls') 
while controlBln == True:
    os.system('cls')
    print('codigo:',codigoInt,'\nNombre:',nombrestr,'\nexistencias:' , existenciasInt)
    opcionStr = input('1.compras\n2. ventas\n3.reportes\n-> ')
    cantidadInt = int(input('cantidad: '))
    if opcionStr == '1':
        existenciasInt += cantidadInt
    if opcionStr =='2':
       if cantidadInt <= existenciasInt:
        existenciasInt -= cantidadInt
       else:
        print('no hay suficientes esxistencias ')
       enter = input('>ENTER<') 
    if opcionStr == '3':
        print('cantidad actual de existencias :',existenciasInt)
    if opcionStr == '4':
        controlBln == False
