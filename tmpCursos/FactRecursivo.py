import math


# numero = int (int(input("ingresar un número para calcular su factorial: ")))
# print(f"El factorial de {numero} es {math.factorial(numero)}")


def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)
    
num = int(input("ingresar un número para calcular su factorial: "))
print(f"El factorial de {num} es {factorial(num)}")