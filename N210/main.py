# Juego de N210 como Proyecto Final
# de Fundamentos de Programación
# Creado por Clara (:

import os
import sys
import json
import random
import pyfiglet
from console.utils import wait_key


# Variables constantes
PARTIDA_DEFAULT: str = "partida.txt"
LEADERBOARD_FILE: str = "leaderboard.txt"
GANADORES_FILE: str = "ganadores.txt"
PANTALLA_LARGO: int = 62


# Limpia la pantalla independientemente del OS
def clear():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")


# Determina la dirección a la cual mover el tablero
def movimiento() -> str:
    while True:
        match wait_key():
        #match input("> ").lower():
            case "w" | "A":
                return "arriba"

            case "a" | "D":
                return "izquierda"

            case "s" | "B":
                return "abajo"

            case "d" | "C":
                return "derecha"

            case "g":
                return "guardar"

            case "q":
                return "salir"


# Determina la posición del tablero al moverlo hacia la derecha
def derecha(tablero: list[int]) -> (list[int], int):
    # Primero hacemos una copia del tablero original
    tablero = [i for i in tablero]

    puntos = 0

    # Prefiero usar índices con un while en vez de un for loop
    # porque puedo agregar optimizaciones si dos o más casillas
    # fueron juntadas, saltándome calculos innecesarios
    # i, j = len(tablero)-1, 0      <--------------------------

    def eliminar_ceros():
        i = len(tablero)-1
        while i >= 0:
            j = 0
            while j < 3:
                # Obtenemos el offset del siguiente
                # número que no sea cero
                k = 0
                while j+k+1 < 4 and tablero[i-j-k] == 0:
                    k += 1

                if tablero[i-j] == 0:
                    tablero[i-j] = tablero[i-j-k]
                    tablero[i-j-k] = 0

                j += 1

            # Vamos de fila en fila (4 en 4) de manera inversa
            i -= 4

    # Eliminamos los 0 a la derecha
    eliminar_ceros()

    # Juntamos los repetidos desde la derecha
    i = len(tablero)-1
    while i >= 0:
        j = 0
        while j < 3:
            if tablero[i-j] == tablero[i-j-1]:
                tablero[i-j] *= 2
                tablero[i-j-1] = 0
                puntos += tablero[i-j]  # Sumamos los puntos adquiridos
                j += 1  # La siguiente casilla está vacía. Sáltemosla
            j += 1

        # Vamos de fila en fila (4 en 4) de manera inversa
        i -= 4

    # Volvemos a eliminar los 0 desde la derecha
    eliminar_ceros()

    return tablero, puntos


# Determina la posición del tablero al moverlo hacia la izquierda
def izquierda(tablero: list[int]) -> (list[int], int):
    # Hacemos una copia del tablero original
    tablero = [i for i in tablero]

    # Le damos la vuelta al tablero
    tablero = [i for i in reversed(tablero)]

    # Aplicamos el algoritmo para mover hacia la derecha
    tablero, puntos = derecha(tablero)

    # Volvemos a voltear el tablero
    tablero = [i for i in reversed(tablero)]

    return tablero, puntos


# Determina la posición del tablero al moverlo hacia abajo
def abajo(tablero: list[int]) -> (list[int], int):
    # Hacemos una copia del tablero original
    tablero = [i for i in tablero]

    def convertir_columnas(tab: list[int]):
        temp: list = []
        for i in range(4):
            for j in range(4):
                temp.append(tab[(j * 4)+i])
        return temp

    # Adaptamos la fila para que quede con columnas
    tablero = convertir_columnas(tablero)

    # Aplicamos el algoritmo de la derecha
    tablero, puntos = derecha(tablero)

    # Regresamos el tablero a la normalidad
    tablero = convertir_columnas(tablero)

    return tablero, puntos


# Determina la posición del tablero al moverlo hacia arriba
def arriba(tablero: list[int]) -> (list[int], int):
    # Hacemos una copia del tablero original
    tablero = [i for i in tablero]

    # Le damos la vuelta al tablero
    tablero = [i for i in reversed(tablero)]

    # Aplicamos el algoritmo para mover hacia abajo
    tablero, puntos = abajo(tablero)

    # Volvemos a voltear el tablero
    tablero = [i for i in reversed(tablero)]

    return tablero, puntos


# Imprime el tablero
def imprimir_tablero(tablero: list[int]) -> None:
    # Hacemos una copia del tablero original
    tablero = [i for i in tablero]

    # Diooooos estááááá aquíííííí
    # Tan cierto como el aire queeeee respiroooo
    # Tan cierto como la mañaaaana se levaaaaantaaaa
    # Tan cierto como que este canto lo puedes oiiiiiiiir
    # ┏━┓
    # ┃ ┃
    # ┗━┛
    # ╋
    # ┳
    # ┻

    espacios = (PANTALLA_LARGO // 2 // 4) - 2
    raya = "━" * espacios
    
    print(("┏" + raya + "┳" + raya + "┳" + raya + "┳" + raya + "┓").center(PANTALLA_LARGO))

    for i in range(4):
        linea = ""
        linea += "┃"
        for j in range(4):
            numero: int = tablero[(i * 4) + j]
            numero: str = str(numero) if numero != 0 else " "
            linea += f"{numero.center(espacios)}"
            if j < 3:
                linea += "┃"
        print(f"{linea}┃".center(PANTALLA_LARGO))

        if i < 3:
            print(("┣" + raya + "╋" + raya + "╋" + raya + "╋" + raya + "┫").center(PANTALLA_LARGO))

    print(("┗" + raya + "┻" + raya + "┻" + raya + "┻" + raya + "┛").center(PANTALLA_LARGO))


# Escribe un diccionario a un archivo
def guardar_datos(filename: str, parametros: dict):
    with open(filename, "w") as file:
        json.dump(parametros, file)


# Recupera un diccionario de un archivo
def leer_datos(filename: str) -> dict:
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, PermissionError):
        return {}


# Utiliza el algoritmo de burbuja para ordenar una lista de enteros
# Esta función ordena de menor a mayor
def sortear_burbuja_min2max(lista: list[int]) -> list[int]:
    # Hacemos una copia de la lista original
    lista = [i for i in lista]

    def esta_sorteado(lista: list[int]) -> bool:
        i = 0
        while i < len(lista)-1:
            if lista[i] > lista[i+1]:
                return False
            i += 1
        return True

    while not esta_sorteado(lista):
        i = 0
        while i < len(lista)-1:
            # Verificamos si el elemento actual es más grande que el siguiente
            if lista[i] > lista[i+1]:
                # Invertimos los elementos
                lista[i], lista[i+1] = lista[i+1], lista[i]
            i += 1

    return lista


# Utiliza el algoritmo de burbuja para ordenar una lista de enteros
# Esta función ordena de mayor a menor
def sortear_burbuja_max2min(lista: list[int]) -> list[int]:
    # Aplicamos el algoritmo de burbuja normal de menor a mayor
    # y simplemente lo devolvemos invertido
    return [i for i in reversed(sortear_burbuja_min2max(lista))]


# Imprime los puntajes de todos los jugadores de mayor a menor
def imprimir_leaderboard(leaderboard: dict) -> None:
    # Imprimimos título épico
    figlet("Leaderboard", font="standard")

    if len(leaderboard) == 0:
        return

    # Obtenemos el nombre más largo en la leaderboard
    espacios = len("Nombre")
    for i in leaderboard:
        if len(i) > espacios:
            espacios = len(i)
    espacios += 5

    raya = "━" * espacios

    # Extraemos los puntajes numéricos de la leaderboard
    puntajes = [(leaderboard[i], i) for i in leaderboard]

    # Vamos a ordenar quién tiene mayor puntaje
    puntajes = sortear_burbuja_max2min(puntajes)

    # Imprimimos el header
    print(("┏" + raya + "┳" + raya + "┓").center(PANTALLA_LARGO))
    linea = "┃"
    linea += f"Nombre".center(espacios)
    linea += "┃"
    linea += f"Puntos".center(espacios)
    linea += "┃"
    print(linea.center(PANTALLA_LARGO))
    print(("┣" + raya + "╋" + raya + "┫").center(PANTALLA_LARGO))
    print(("┣" + raya + "╋" + raya + "┫").center(PANTALLA_LARGO))

    # Los imprimimos de mayor a menor
    c = 0
    for i in puntajes:
        c += 1

        linea = "┃"
        linea += f"{i[1]}".center(espacios)
        linea += "┃"
        linea += f"{i[0]}".center(espacios)
        linea += "┃"

        print(linea.center(PANTALLA_LARGO))

        if c < len(leaderboard):
            print(("┣" + raya + "╋" + raya + "┫").center(PANTALLA_LARGO))

    print(("┗" + raya + "┻" + raya + "┛").center(PANTALLA_LARGO))


# Imprime a todos los ganadores y su número de victorias de menor a mayor
def imprimir_ganadores(ganadores: dict) -> None:
    # Imprimimos título épico
    figlet("Ganadores", font="standard")

    if len(ganadores) == 0:
        return

    # Obtenemos el nombre más largo en la ganadores
    espacios = len("Victorias")
    for i in ganadores:
        if len(i) > espacios:
            espacios = len(i)
    espacios += 5

    raya = "━" * espacios

    # Extraemos los puntajes numéricos de la ganadores
    victorias = [(ganadores[i], i) for i in ganadores]

    # Vamos a ordenar quién tiene mayor puntaje
    victorias = sortear_burbuja_min2max(victorias)

    # Imprimimos el header
    print(("┏" + raya + "┳" + raya + "┓").center(PANTALLA_LARGO))
    linea = "┃"
    linea += f"Nombre".center(espacios)
    linea += "┃"
    linea += f"Victorias".center(espacios)
    linea += "┃"
    print(linea.center(PANTALLA_LARGO))
    print(("┣" + raya + "╋" + raya + "┫").center(PANTALLA_LARGO))
    print(("┣" + raya + "╋" + raya + "┫").center(PANTALLA_LARGO))

    # Los imprimimos de mayor a menor
    c = 0
    for i in victorias:
        c += 1

        linea = "┃"
        linea += f"{i[1]}".center(espacios)
        linea += "┃"
        linea += f"{i[0]}".center(espacios)
        linea += "┃"

        print(linea.center(PANTALLA_LARGO))

        if c < len(ganadores):
            print(("┣" + raya + "╋" + raya + "┫").center(PANTALLA_LARGO))

    print(("┗" + raya + "┻" + raya + "┛").center(PANTALLA_LARGO))


# Presenta al usuario con opciones a realizar
def menu() -> int:
    clear()

    while True:
        print("Bienvenido a N210. Seleccione una opción:")
        print(f"[0] Iniciar nueva partida")
        print(f"[1] Continuar partida guardada")
        print(f"[2] Mostrar ganadores")
        print(f"[3] Mostrar puntajes")
        seleccion = input("> ")

        if not seleccion.isnumeric():
            clear()
            print("[!] Opción inválida. Por favor, intente de nuevo.\n")
            continue

        if 0 <= int(seleccion) <= 3:
            break

        clear()
        print("[!] Opción inválida. Por favor, intente de nuevo.\n")

    clear()
    return int(seleccion)


# Solicita al usuario el valor de n
def obtener_n() -> int:
    while True:
        n = input("Ingrese el valor de N [1-10]: ")

        # Nos aseguramos de que el input ingresado es un valor numérico
        if not n.isnumeric():
            clear()
            print("[!] Por favor, ingrese un valor numérico entre 1 y 10.\n")
            continue

        # También nos aseguramos de que esté entre 1 y 10
        if not 1 <= int(n) <= 10:
            clear()
            print("[!] Por favor, ingrese un valor numérico entre 1 y 10.\n")
            continue

        return int(n)


# Imprime una bienvenida con las instrucciones
def imprimir_instrucciones(n: int, new=True) -> None:
    separador = "=============================================================="
    longitud = len(separador)

    print(separador)
    print(f"¡Bienvenido{' ' if new else ' de vuelta '}a {n * 2 ** 10}!".center(longitud))
    print()
    print("¿Cómo jugar?".center(longitud))
    print("Arriba [W], Izquierda [A], Abajo [S], Derecha [D], Guardar [G]".center(longitud))
    print(f"Además de WASD, también puedes utilizar las flechas ←↓↑→".center(longitud))
    print(f"Presiona [Q] en cualquier momento para salir sin guardar".center(longitud))
    print(separador)


# Agrega una casilla aleatoria al tablero
def casilla_aleatoria(tablero: list, tablero_anterior: list, n: int) -> list[int]:
    # Si no ha habido ningún cambio, no hagamos nada
    if tablero == tablero_anterior:
        return tablero

    # Creamos una copia del tablero original
    tablero = [i for i in tablero]

    # Obtenemos todas las casillas vacías
    posiciones_vacias = [i for i, x in enumerate(tablero) if x == 0]

    # Comprobamos si hay casillas disponibles
    if len(posiciones_vacias) == 0:
        # No hay casillas disponibles. No hagamos nada
        return tablero

    # Seleccionamos una casilla aleatoria
    # Le agregamos N o 2N (también de manera aleatoria)
    # tablero[random.choice(posiciones_vacias)] = n if random.randint(0, n * 2 ** 10) % 2 == 0 else 2 * n
    tablero[random.choice(posiciones_vacias)] = random.choice([n, 2 * n])

    return tablero


# Esta función facilita decidir dónde guardar la partida
# Devuelve True si la partida fue guardada y False si no
def guardar_partida(nombre: str, n: int, puntaje: int, tablero: list[int], tablero_anterior: list[int], sandbox: bool) -> bool:
    clear()

    print("Ingrese el nombre del archivo donde desea guardar su partida")
    archivo = input("Nombre del archivo [partida.txt]: ")

    if archivo == "":
        # Utilizamos el default
        archivo = PARTIDA_DEFAULT

    # Verificamos si el archivo ya existe
    if os.path.exists(archivo):
        print(f"{archivo} ya existe. Desea sobreescribirlo? [Y/n] ")
        decision = input("> ").lower()

        if decision == "n":
            return False

    # Guardamos todos los parametros para recuperar la partida
    guardar_datos(archivo, {
        "nombre": nombre,
        "n": n,
        "puntaje": puntaje,
        "tablero": tablero,
        "tablero_anterior": tablero_anterior,
        "sandbox": sandbox,
    })

    clear()
    print("Su partida ha sido guardada. ¡Hasta luego!")
    return True


# Esta función devuelve True si el tablero contiene una posición ganadora
# De lo contrario, devuelve False
def comprobar_victoria(tablero: list[int], n: int) -> bool:
    # Si n se encuentra en el tablero, el jugador ha ganado
    # Si no, el juego continúa (o el jugador ha perdido)
    return n * 2 ** 10 in tablero


# Esta función devuelve True si el tablero se ha quedado sin movimientos
# De lo contrario, devuelve False
def comprobar_derrota(tablero: list[int]) -> bool:
    # Primero comprobamos si hay casillas libres
    if 0 in tablero:
        # Hay casillas libres
        return False

    # Comprobamos si es posible mover hacia arriba
    _, puntos = arriba(tablero)
    if puntos > 0:
        # Si se puede
        return False

    # Comprobamos si es posible mover hacia la izquierda
    _, puntos = izquierda(tablero)
    if puntos > 0:
        # Si se puede
        return False

    # Comprobamos si es posible mover hacia abajo
    _, puntos = abajo(tablero)
    if puntos > 0:
        # Si se puede
        return False

    # Comprobamos si es posible mover hacia la derecha
    _, puntos = derecha(tablero)
    if puntos > 0:
        # Si se puede
        return False

    # No hay movimientos posibles ni casillas libres
    # El jugador ha perdido. F
    return True


# Imprime texto de manera bonita
def figlet(texto: str, font="basic", center=True) -> None:
    formato = pyfiglet.figlet_format(texto, font=font)
    if center:
        formato = formato.center(PANTALLA_LARGO)
    print(formato)


def main():
    nombre: str = ""
    n: int = 0
    puntaje: int = 0
    new: bool = True
    sandbox: bool = False
    victoria: bool = False

    # Creamos un tablero vacío
    tablero = [0 for _ in range(16)]
    tablero_anterior = [-1 for _ in range(16)]

    # Jesucristo cómo me gustaría que el IDE me dejara colapsar los case

    # Muestra el menu y selecciona la operación que vamos a realizar
    match menu():
        # Iniciamos nueva partida
        case 0:
            # Le solicitamos el valor de N al usuario
            n = obtener_n()
            new = True  # Nueva partida

        # Continuamos partida guardada
        case 1:
            print("Indique el nombre del archivo con su partida guardada")
            archivo = input(f"Nombre del archivo [{PARTIDA_DEFAULT}]: ")

            if archivo == "":
                # Utilizamos el default
                archivo = PARTIDA_DEFAULT

            # Recuperamos la partida
            partida = leer_datos(archivo)

            # Vamos a asignar cada parametro que tenemos a aquellos guardados
            # en el archivo. En caso de que haya habido algún error leyéndolo,
            # falte algún parámetro o la partida no exista, crearemos una nueva partida
            # asignando valores default a las variables
            nombre = partida.get("nombre", "")
            n = partida.get("n", -1)
            puntaje = partida.get("puntaje", 0)
            tablero = partida.get("tablero", tablero)
            tablero_anterior = partida.get("tablero_anterior", tablero_anterior)
            sandbox = partida.get("sandbox", False)

            if n == -1:
                print(f"\n[*] Atención: El archivo '{archivo}' no existe o no contiene una partida válida.")
                print(f"    Se iniciará una nueva partida desde cero.\n")
                n = obtener_n()

            if tablero.count(0) == 16:
                new = True
            else:
                new = False     # Partida continuada

        # Mostramos ganadores y salimos
        case 2:
            clear()

            # Primero obtenemos la lista de ganadores
            ganadores = leer_datos(GANADORES_FILE)
            imprimir_ganadores(ganadores)
            return

        # Mostramos puntajes y salimos
        case 3:
            clear()

            # Primero obtenemos la lista de puntajes
            leaderboard = leer_datos(LEADERBOARD_FILE)
            imprimir_leaderboard(leaderboard)
            return

    # Agregamos una casilla aleatoria inicial al tablero
    tablero = casilla_aleatoria(tablero, tablero_anterior, n)

    # Gameloop
    while True:
        clear()

        # Agregamos una casilla aleatoria
        tablero = casilla_aleatoria(tablero, tablero_anterior, n)

        # Guardamos el viejo valor del tablero
        tablero_anterior = tablero

        # Comprobamos si el usuario ha ganado o ha perdido
        if comprobar_victoria(tablero, n) and not sandbox:
            victoria = True

            # Imprimimos un mensaje de victoria épico
            figlet("Victoria")

            # Mostramos el tablero y el puntaje una última vez
            # para que el usuario vea cómo quedó
            print(f"Puntaje: {puntaje}".center(PANTALLA_LARGO))
            imprimir_tablero(tablero)

            print()
            print("¡Has ganado! Felicitaciones.")

            # Si no lo tenemos, le solicitamos el nombre al usuario
            while nombre == "":
                nombre = input("Por favor, ingresa tu nombre: ")

            # Obtenemos las victorias que lleva el usuario
            ganadores = leer_datos(GANADORES_FILE)
            victorias = ganadores.get(nombre, 0) + 1
            print(f"¡Vaya, con esta ya has ganado {victorias} {'veces' if victorias > 1 else 'vez'}, {nombre}!")

            # Actualizamos el registro
            ganadores[nombre] = victorias
            guardar_datos(GANADORES_FILE, ganadores)
            print("Tu registro de victorias se ha actualizado.")

            # Consideramos entrar en modo sandbox
            if input("\nDeseas continuar en modo Sandbox? [Y/n] ").lower() == "n":
                sandbox = False
                break

            sandbox = True
            tablero_anterior = tablero  # Evita agregar 2 nuevas casillas aleatorias
            continue

        elif comprobar_derrota(tablero):
            victoria = False

            # Imprimimos un mensaje de derrota épico, a menos que
            # estemos en modo sandbox, en cuyo caso ya ganamos
            if not sandbox:
                figlet("Derrota")

            # Mostramos el tablero y el puntaje una última vez
            # para que el usuario vea cómo quedó
            print(f"Puntaje: {puntaje}".center(PANTALLA_LARGO))
            imprimir_tablero(tablero)

            # Si estamos en modo sandbox, en realidad ya ganamos
            if sandbox:
                break

            print()
            print("Lo lamento. ¡Has perdido!")

            # Si no lo tenemos, le solicitamos el nombre al usuario
            while nombre == "":
                nombre = input("Por favor, ingresa tu nombre: ")

            break

        # Imprimimos las instrucciones
        imprimir_instrucciones(n, new=new)

        # Imprimimos un indicador de modo sandbox si hace falta
        if sandbox:
            print("(Modo Sandbox)".center(PANTALLA_LARGO))

        # Mostramos el tablero y el puntaje
        print(f"Puntaje: {puntaje}".center(PANTALLA_LARGO))
        imprimir_tablero(tablero)

        # Le pedimos al usuario que ingrese su siguiente movimiento
        match movimiento():
            case "arriba":
                tablero, puntos = arriba(tablero)
                puntaje += puntos

            case "izquierda":
                tablero, puntos = izquierda(tablero)
                puntaje += puntos

            case "abajo":
                tablero, puntos = abajo(tablero)
                puntaje += puntos

            case "derecha":
                tablero, puntos = derecha(tablero)
                puntaje += puntos

            case "guardar":
                if guardar_partida(nombre, n, puntaje, tablero, tablero_anterior, sandbox):
                    return

            case "salir":
                return

    # La partida ha terminado
    # Vamos a hacer todo el papeleo con los puntajes
    print(f"La partida ha terminado con {puntaje}. ", end='')

    # Obtenemos el puntaje más alto del usuario
    leaderboard: dict = leer_datos(LEADERBOARD_FILE)
    mas_alto: int = leaderboard.get(nombre, 0)

    if puntaje > mas_alto:
        print("¡Nuevo record!")
        mas_alto = puntaje
    else:
        print(f"Tu puntaje más alto es de {mas_alto} puntos.")

    # Imprimimos un mensajito dependiendo de si el usuario ganó o perdió
    if not victoria and not sandbox:
        print(f"Mejor suerte para la próxima, {nombre}!")
    else:
        print(f"Felicitaciones, {nombre}!")

    # Actualizamos la leaderboard
    leaderboard[nombre] = mas_alto
    guardar_datos(LEADERBOARD_FILE, leaderboard)
    print("La leaderboard ha sido actualizada.")
    print("¡Gracias por jugar!")


if __name__ == '__main__':
    main()
