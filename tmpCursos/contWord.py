#El objetivo de codigo es contar el numero de palabras en una cadena de caracteres
#El usuario debe ingresar una cadena de caracteres
#Se debe imprimir el numero de palabras en la cadena de caracteres

#importamos la libreria re para utilizar expresiones regulares
import re

def contWord(cadena):
    numPalabras = re.findall(r'\b\w+\b', cadena)
    #contar palabras
    conteo = len(numPalabras)
    print(f"El numero de palabras en la cadena de caracteres es: {conteo}")

cadena = input("Ingresar cadena de caracteres: ")
contWord(cadena)

# import re  # Asegúrate de importar el módulo re

# def contWord(cadena):
#     # Buscar las palabras utilizando una expresión regular
#     numPalabras = re.findall(r'\b\w+\b', cadena)
#     # Contar las palabras
#     conteo = len(numPalabras)
#     # Imprimir el conteo de palabras
#     print(f"El número de palabras en la cadena de caracteres es: {conteo}")

# # Solicitar entrada al usuario
# cadena = input("Ingresar cadena de caracteres: ")
# contWord(cadena)