# Programa que convierte números romanos a números arábigos
def numeros_romanos():
    # Le solicitamos la entrada en romano al usuario
    romanos = input("Ingrese una cifra en números romanos: ")

    numero_previo = 0
    resultado = 0

    # Evaluamos cada caracter del romano
    for i in romanos:
        # Lo traducimos a su equivalente arábigo
        match i:
            case 'I':   # 1
                resultado += 1
                numero_previo = 1

            case 'V':   # 5
                if numero_previo == 1:
                    # I puede ser usado antes de V para escribir 4.
                    # De esa forma, solo tenemos que sumar 3 para llegar al 4
                    # ya que 1 ya fue sumado en la iteración anterior que era I.
                    resultado += 3

                else:
                    resultado += 5

                numero_previo = 5

            case 'X':   # 10
                if numero_previo == 1:
                    # I puede ser usado antes de X para escribir 9.
                    # De esa forma, solo tenemos que sumar 8 para llegar al 9
                    # ya que 1 ya fue sumado en la iteración anterior que era I.
                    resultado += 8

                else:
                    resultado += 10

                numero_previo = 10

            case 'L':   # 50
                if numero_previo == 10:
                    # X puede ser usado antes de L para escribir 40.
                    # De esa forma, solo tenemos que sumar 30 para llegar al 40
                    # ya que 10 ya fue sumado en la iteración anterior que era X.
                    resultado += 30

                else:
                    resultado += 50

                numero_previo = 50

            case 'C':   # 100
                if numero_previo == 10:
                    # X puede ser usado antes de C para escribir 90.
                    # De esa forma, solo tenemos que sumar 80 para llegar al 90
                    # ya que 10 ya fue sumado en la iteración anterior que era X.
                    resultado += 80

                else:
                    resultado += 100

                numero_previo = 100

            case 'D':   # 500
                if numero_previo == 100:
                    # C puede ser usado antes de D para escribir 400.
                    # De esa forma, solo tenemos que sumar 300 para llegar al 400
                    # ya que 100 ya fue sumado en la iteración anterior que era C.
                    resultado += 300

                else:
                    resultado += 500

                numero_previo = 500

            case 'M':   # 1000
                if numero_previo == 100:
                    # C puede ser usado antes de M para escribir 900.
                    # De esa forma, solo tenemos que sumar 800 para llegar al 900
                    # ya que 100 ya fue sumado en la iteración anterior que era C.
                    resultado += 800

                else:
                    resultado += 1000

                numero_previo = 1000

            case _:
                # Si el usuario ha ingresado un caracter inválido,
                # abortamos todas las operaciones y le asignamos
                # al resultado el error para imprimirlo
                resultado = f"Caracter romano no válido -- '{i}'"
                break

    # Imprimimos el resultado
    print(resultado)


if __name__ == '__main__':
    numeros_romanos()

