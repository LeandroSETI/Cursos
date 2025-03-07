import math


# numero = int (int(input("ingresar un número para calcular su factorial: ")))
# print(f"El factorial de {numero} es {math.factorial(numero)}")


def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1) 
# el codigo llama a la definicion de la funcion factorial, es decir, se llama a si misma
# en este caso se llama a si mismo desde 5 y va restando 1 hasta llegar a 1
    
num = int(input("ingresar un número para calcular su factorial: "))
print(f"El factorial de {num} es {factorial(num)}")