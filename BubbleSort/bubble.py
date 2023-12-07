def sorteado(array: list):
    # Iteramos cada elemento de la lista y lo comparamos con el de arriba
    # Si detecta una discrepancia, la lista no está sorteada e inmediatamente salimos.
    # Si llega al final del arreglo sin problemas es porque está sorteada.
    i = 0
    while i < len(array)-1:
        if array[i] > array[i+1]:
            return False
        i += 1
    return True

def bubble(array: list):
    # Hacemos una copia de la lista original para
    # evitar modificar sus valores originales
    array = [i for i in array]

    # Vamos a ir elemento por elemento comparándolo con el de arriba
    while not sorteado(array):
        i = 0
        while i < len(array)-1:
            # Si el elemento actual es mayor al de arriba, está desordenado,
            # En dado caso, intercambiamos los elementos, ordenando la parejita.
            if array[i] > array[i+1]:
                # Intercambiamos los valores
                array[i], array[i+1] = array[i+1], array[i]
            i += 1

    return array

def main():
    # Le preguntamos al usuario los nombres de los archivos
    # de donde leer la lista desordenada y escribir la ordenada
    desordenada_filename = input("Ingrese el nombre del archivo donde leer la lista desordenada: ")
    ordenada_filename = input("Ingrese el nombre del archivo a donde escribir la lista sorteada: ")

    # En realidad no hace falta declararla aquí pero bueno
    lista = list()

    # Abrimos el archivo para leer la lista sin sortear
    # Este programa no atrapa escenarios donde abrir el archivo falla por falta de permisos
    # o porque el archivo no existe. Para eso tendríamos que usar un try pero como no lo
    # hemos visto prefiero no usarlo por ahora
    with open(desordenada_filename, "r") as file:
        # Leemos el archivo de golpe
        lista = file.read()

    # Convertimos la lectura como string a una lista
    lista = lista.strip().split('\n')

    # Ahora tenemos una lista de strings
    # Vamos a convertir todos los elementos a enteros
    lista = [int(i) for i in lista]

    # Sorteamos la lista a través de Bubble Sort
    lista = bubble(lista)

    # Escribimos el resultado a un archivo
    # Nuevamente, este programa no atrapa escenarios donde abrir el archivo falla.
    with open(ordenada_filename, "w+") as file:
        # Escribimos cada elemento de la lista sorteada al archivo
        for i in lista:
            file.write(f"{i}\n")


if __name__ == '__main__':
    main()

