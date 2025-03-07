#primero se crea un diccionario con el codigo morse

morse_code = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',    
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---', 
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---', 
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',  'T': '-',    
    'U': '..-',   'V': '...-', 'W': '.--',   'X': '-..-',  'Y': '-.--', 
    'Z': '--..',  

    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '\'': '.----.', '!': '-.-.--',
    '/': '-..-.',  '(': '-.--.',  ')': '-.--.-', '&': '.-...',  ':': '---...', 
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.',  '-': '-....-', '_': '..--.-', 
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}

#se crea una funcion que recibe un mensaje y lo convierte a codigo morse
def convertir_a_morse(mensaje):
    mensaje = mensaje.upper()  # Convertir el mensaje a mayúsculas
    mensaje_morse = ""

    # Recorrer cada carácter del mensaje
    for char in mensaje:
        if char in morse_code:  # Verificar si el carácter está en el diccionario
            mensaje_morse += morse_code[char] + " "  # Agregar el código Morse seguido de un espacio
        else:
            mensaje_morse += " "  # Si no está en el diccionario (como un espacio en blanco), agregar un espacio

    return mensaje_morse.strip()  # Eliminar el espacio final sobrante

mensaje = input("ingresa la cadena de caracteres a transformar a morse: ")
codigo_morse = convertir_a_morse(mensaje)
print(f"Mensaje: {mensaje}")
print(f"Código Morse: {codigo_morse}")
