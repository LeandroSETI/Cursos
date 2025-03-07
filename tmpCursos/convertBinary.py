# def convertBinary(Num):
#     if Num > 1:
#         convertBinary(Num // 2)
#     print(Num % 2, end='') 

# # tomar el numero decimal del usuario
# decimal = int(input("Ingrese un numero decimal: "))
# convertBinary(decimal)

#sin usar funciones recursivas
def convertBinary(Num):
    binary = ""
    while Num > 0:
        binary = str(Num % 2) + binary
        Num = Num // 2
    return binary