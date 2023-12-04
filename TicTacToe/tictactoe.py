import sys
import os

### Juego de Tic Tac Toe con dos jugadores humanos ###

# Limpiar la pantalla independientemente del OS del usuario
def clear():
    # Comprobamos el Sistema Operativo del usuario
    if sys.platform == 'win32':
        # El usuario está usando Windows
        os.system("cls")
    else:
        # El usuario probablemente esté en algún sistema Unix
        os.system("clear")


# Imprimir un tablero de TicTacToe dadas las posiciones
def imprimir_tablero(posiciones: list):
    for i in range(0, 3):
        for j in range(0, 3):
            print(f" {posiciones[(i*3)+j]}", end="")
            if j < 2:
                print(" ┃", end="")
        if i < 2:
            print(f"\n━━━╋━━━╋━━━")
    print()


# Convierte coordenadas (X, Y) en un índice de un arreglo unidimensional
# Aquí estamos asumiendo que el número de columnas es 3 por el juego
def coords(x: int, y: int, columnas: int = 3):
    return (y * columnas) + x


# Función que determina si el juego continúa o termina, y en dado caso
# de terminar, devuelve el resultado de la partida
def comprobar_ganador(posiciones: list):
    # Primero comprobamos si hay 3 continuas horizontales
    for i in range(0, 3):
        if posiciones[coords(0, i)] == posiciones[coords(1, i)] == posiciones[coords(2, i)] and posiciones[coords(0, i)] != " ":
            # Alguien ganó en horizontal. Devolvemos el que fue
            return posiciones[coords(0, i)]

    # Luego comprobamos si hay 3 continuas verticales
    for i in range(0, 3):
        if posiciones[coords(i, 0)] == posiciones[coords(i, 1)] == posiciones[coords(i, 2)] and posiciones[coords(i, 0)] != " ":
            # Alguien ganó en vertical. Devolvemos el que fue
            return posiciones[coords(i, 0)]

    # Luego comprobamos si hay 3 continuas en la diagonal izquierda-derecha
    if posiciones[0] == posiciones[4] == posiciones[8] and posiciones[0] != " ":
        # Alguien ganó en diagonal izquierda-derecha. Devolvemos el que fue
        return posiciones[0]

    # Luego comprobamos si hay 3 continuas en la diagonal derecha-izquierda
    if posiciones[2] == posiciones[4] == posiciones[6] and posiciones[2] != " ":
        # Alguien ganó en diagonal derecha-izquierda. Devolvemos el que fue
        return posiciones[2]

    # Si ninguno de los dos ha ganado pero YA NO hay casillas disponibles, entonces el juego termina en empate.
    # Los espacios disponibles están representados con un espacio
    if " " not in posiciones:
        return "Empate"

    # Si ninguno de los dos ha ganado pero todavía hay casillas disponibles, entonces el juego continúa.
    # Utilizaremos None para representar que no hay ningún ganador (todavía), empate incluído
    return None


# El juego
def tic_tac_toe():
    # Inicializamos un tablero vacío
    posiciones = [" " for i in range(0, 9)]

    # Representaremos el turno actual con un valor booleano,
    # donde True representa el turno de las X y False el de las O
    turno_X = True

    clear()

    ganador = None

    # Mainloop del juego
    while True:
        jugador = 'X' if turno_X else 'O'

        # Imprimimos la UI
        imprimir_tablero(posiciones)

        # Verificamos si hay algún ganador de la iteración anterior del loop
        ganador = comprobar_ganador(posiciones)
        if ganador != None:
            break

        # Le solicitamos el input al usuario
        movimiento = input(f"\nTurno del jugador {jugador}. Elige una posición (1-3, 1-3): ")

        # Sanitizamos y procesamos el input
        movimiento = movimiento.replace(" ", "")        # Removemos espacios en blanco
        fila, columna = movimiento.split(",")[0:2]      # Extraemos la fila y columna del input ignorando el exceso

        # Verificamos si el input es válido
        if not fila.isnumeric() or not columna.isnumeric():
            # El jugador introdujo unas coordenadas inválidas.
            # Le avisamos y no nos saltamos su turno.
            # Interrumpimos la iteración actual.
            clear()
            print("[!] Por favor ingrese un movimiento válido.\n")
            continue

        # Convertimos los valores de las filas y columnas a entero y le restamos
        # 1 porque empezamos a contar desde cero
        fila, columna = int(fila)-1, int(columna)-1

        # Verificamos si las coordenadas ingresadas son válidas
        if not 0 <= fila <= 2 or not 0 <= columna <= 2:
            # El jugador introdujo coordenadas o muy chiquitas o muy grandes.
            # Le pedimos que las introduzca de nuevo sin saltarnos su turno.
            clear()
            print("[!] Las coordenadas que ha ingresado son inválidas. Por favor, intente de nuevo.\n")
            continue

        # Verificamos si la casilla ya estaba ocupada
        if posiciones[coords(columna, fila)] != " ":
            # El jugador ha tratado de jugar en una casilla ya usada.
            # Le avisamos y le pedimos que introduzca otra distinta,
            # pero no nos saltamos su turno.
            clear()
            print("[!] La casilla que ha introducido ya está usada. Por favor, escoga otra.\n")
            continue

        # Insertamos el movimiento del jugador en las posiciones
        posiciones[coords(columna, fila)] = jugador

        # Invertimos el valor de verdad de la variable que rastrea el turno
        # para pasarle el turno al jugador opuesto al actual.
        turno_X = not turno_X

        clear()

    # El juego ha terminado. Verificamos el ganador
    # Coloco este chequeo al final del juego después del loop para que no se tenga
    # que revisar en cada iteración, sino 1 sola vez al final de la partida.
    if ganador != "Empate":
        print(f"\n¡El jugador {ganador} ha ganado!")
    else:
        print(f"\n¡El juego ha terminado en empate!")


if __name__ == '__main__':
    tic_tac_toe()

