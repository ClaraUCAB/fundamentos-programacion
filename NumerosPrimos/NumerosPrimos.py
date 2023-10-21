# Programa para calcular si un número es primo o no
def NumerosPrimos():
    # Le solicitamos un número entero al usuario
    numero = int(input("Por favor, ingrese un número: "))

    # Primero podemos descartar todos los números que no sean mayores a 1
    if not numero > 1:
        print(f"El número {numero} no es primo.")
        return

    # Ahora podemos iterar entre todos los números del 2 hasta la raíz cuadrada del número.
    # Es suficiente llegar hasta la raíz y no el rango completo ya que tratando de encontrar
    # factores que dividan al número del usuario, números más allá de su raíz no pueden multiplicarse
    # para componer al número exacto, y por lo tanto podemos descartarlos automáticamente.
    # De esta forma nos ahorramos una cantidad gigantezca de ciclos y nuestro programa es más eficiente.
    # Si ninguno de los números del 2 a su raíz es factor suyo, eso solo deja a 1 y a sí mismo como factores,
    # lo que significa que sí es primo, y si sí hay algún factor además de 1 y sí mismo, entonces no es primo.

    # Con esto podemos iterar hasta la raíz del número del usuario
    i = 2
    while i*i <= numero:
        # Comprobamos si el número es divisible entre i o no
        # Si es divisible, entonces no es primo
        if numero % i == 0:
            print(f"El número {numero} no es primo.")
            return

        i += 1

    # Si el número no es divisible entre ninguno de los números que intentamos,
    # excepto 1 y sí mismo, el número es primo.
    print(f"El número {numero} sí es primo.")
    return


if __name__ == '__main__':
    NumerosPrimos()

