def convertBinary(Num):
    if Num > 1:
        convertBinary(Num // 2)
    print(Num % 2, end='')

# tomar el numero decimal del usuario
decimal = int(input("Ingrese un numero decimal: "))
convertBinary(decimal)

#imprimir el nuevo numero binario