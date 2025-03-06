
# ejercicio concatenación
# -Como concatenar dos datos numericos
# dato 1: 7
# dato 2: 10

# "7"+"10" -> el resultado de la concatenación es "710"

# ejercicio booleanos
# Ver en Notes

array_Edades = [5, 10, 20, 18]

# Usando un bucle for con el índice adecuado
for i in range(4):
    if array_Edades[i] >= 18:  # Se usa corchetes para acceder al valor
        print(f"La edad {array_Edades[i]} es mayor de edad")
    else:
        print(f"La edad {array_Edades[i]} no es mayor de edad")

#usando while
array_Edades = [5, 10, 20, 18]

# Usando un bucle while con un índice
i = 0
while i < len(array_Edades):  # Mientras el índice sea menor que el tamaño de la lista
    if array_Edades[i] > 18:
        print(f"La edad {array_Edades[i]} es mayor de edad")
    else:
        print(f"La edad {array_Edades[i]} no es mayor de edad")
    i += 1  # Incrementamos el índice
    #Se termina la codificación y se carga la data al repo