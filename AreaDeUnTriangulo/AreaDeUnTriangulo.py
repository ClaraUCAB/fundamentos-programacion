# Programa para calcular el área de un triángulo
def AreaDeUnTriangulo():
    # Definimos las variables para operar
    # No es necesario en python
    base: int
    altura: int
    resultado: int

    # Leemos el valor de la base y la altura del triángulo
    base = int(input("Por favor ingrese la base del triángulo: "))
    altura = int(input("Por favor ingrese la altura del triángulo: "))

    # Aplicamos la fórmula para el área del triángulo
    resultado = (base * altura) / 2

    # Imprimimos el resultado a la pantalla
    print(f"El triángulo tiene un área de: {resultado}")


if __name__ == '__main__':
    AreaDeUnTriangulo()

