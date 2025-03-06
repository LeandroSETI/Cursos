def AreaPol(Poligono):
    if Poligono == "triangulo":
        Base = float(input("Por favor ingrese el valor de la base del triangulo : "))
        Altura = float(input("Por favor ingrese el valor de la altura del triangulo : "))
        area = (Base * Altura)/2    
        return f"El área del triángulo es: {area} unidades cuadradas."
    elif Poligono == "cuadrado":
        Lado = float(input("Por favor ingrese la dimension de un lado del cuadrado : "))
        area = (Lado * Lado)
        return f"El área del triángulo es: {area} unidades cuadradas."
    elif Poligono == "Rectangulo":
        Base = float(input("Por favor ingrese el valor de la base del Rectangulo : "))
        Altura = float(input("Por favor ingrese el valor de la Altura del Rectangulo : "))
        area = (Base * Altura)
        return f"El área del triángulo es: {area} unidades cuadradas."
    else:
        print ("El poligono ingresado no esta soportado. Usar triangulo, cuadrado o rectangulo")

#Solicitar al usuario que ingrese el tipo de poligono

Poligono = input("Por favor ingrese el tipo de poligono a verificar (cuadrado, triangulo, rectangulo)").lower()

AreaPol(Poligono)