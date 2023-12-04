// Juego de Tic Tac Toe con dos jugadores humanos
// Lamento profundamente lo que sus ojos estan a punto de presenciar.
// Este codigo es la maxima expresion de lobotomia y perdida de la cordura.

// Imprimir un tablero de TicTacToe dadas las posiciones
SubProceso ImprimirTablero(posiciones)
    Definir i, j como Entero;

    Para i<-1 Hasta 3
        Para j<-1 Hasta 3
            Escribir Sin Saltar " ", posiciones[Coordenadas(i, j, 3)];
            Si j < 3 Entonces
                Escribir Sin Saltar " |";
            FinSi
		FinPara
		
        Si i < 3 Entonces
			Escribir "";	// \n
            Escribir "---+---+---";
        FinSi	
	FinPara
	
    Escribir "";
FinSubProceso


// Funcion que toma una cadena y reemplaza cada instancia de una subcadena por otra
// Basicamente el .replace de Python
SubProceso nuevo<-Remplazar(original, substr, reemplazo)
	Definir i, originalLen, substrLen Como Entero;
	
	originalLen <- Longitud(original);
	substrLen <- Longitud(substr);
	
	nuevo <- "";
	
	Para i<-1 Hasta originalLen Hacer
		Si i + substrLen <= originalLen Entonces
			Si Subcadena(original, i, i+substrLen-1) = substr Entonces
				nuevo <- Concatenar(nuevo, reemplazo);
				i <- i + substrLen - 1;
			SiNo
				nuevo <- Concatenar(nuevo, Subcadena(original, i, i));
			FinSi
		SiNo
			nuevo <- Concatenar(nuevo, Subcadena(original, i, i));
		FinSi
	FinPara
FinSubProceso


// Convierte coordenadas (X, Y) en un indice de un arreglo unidimensional
// Aqui me encantaria poder asumir que el numero de columnas es 3 por el juego,
// pero no puedo porque esto es pseudocodigo y no Python. Diablos.
// Jesucristo. "Y" es una keyword reservada en PSeInt. Me voy a matar.
Funcion c<-Coordenadas(x, _y, columnas)
	x <- x - 1;
	_y <- _y - 1;
	
    c <- ((_y * columnas) + x) + 1;
FinFuncion


// Funcion que determina si el juego continua o termina, y en dado caso
// de terminar, devuelve el resultado de la partida
Funcion ganador<-ComprobarGanador(posiciones)
    Definir i como Entero;
	
	ganador <- "Empate";

    Para i<-1 Hasta 3
        // Primero comprobamos si hay 3 continuas horizontales
        Si posiciones[Coordenadas(1, i, 3)] = posiciones[Coordenadas(2, i, 3)] Y posiciones[Coordenadas(2, i, 3)] = posiciones[Coordenadas(3, i, 3)] Y posiciones[Coordenadas(1, i, 3)] <> " " Entonces
            // Alguien gano en horizontal. Asignamos a ganador el que fue
            ganador <- posiciones[Coordenadas(1, i, 3)];
        FinSi
		
		// Luego comprobamos si hay 3 continuas verticales
		Si posiciones[Coordenadas(i, 1, 3)] = posiciones[Coordenadas(i, 2, 3)] Y posiciones[Coordenadas(i, 2, 3)] = posiciones[Coordenadas(i, 3, 3)] Y posiciones[Coordenadas(i, 1, 3)] <> " " Entonces
			// Alguien gano en vertical. Asignamos a ganador el que fue
			ganador <- posiciones[Coordenadas(i, 1, 3)];
		FinSi
	FinPara

    // Luego comprobamos si hay 3 continuas en la diagonal izquierda-derecha
    Si posiciones[1] = posiciones[5] Y posiciones[5] = posiciones[9] Y posiciones[1] <> " " Entonces
        // Alguien gano en diagonal izquierda-derecha. Asignamos a ganador el que fue
        ganador <- posiciones[1];
	FinSi

    // Luego comprobamos si hay 3 continuas en la diagonal derecha-izquierda
    Si posiciones[3] = posiciones[5] Y posiciones[5] = posiciones[7] Y posiciones[3] <> " " Entonces
        // Alguien gano en diagonal derecha-izquierda. Asignamos a ganador el que fue
        ganador <- posiciones[3];
	FinSi

	
	// Si ninguno de los dos ha ganado pero todavia hay casillas disponibles, entonces el juego continua.
	// Los espacios disponibles estan representados con un espacio
	i <- 1;
	Mientras i <= 9 Hacer
		Si posiciones[i] == " " Y ganador == "Empate" Entonces
			// No hay empate. Todavia hay casillas libres
			ganador <- "Nadie";
			i <- 9;
		FinSi
		
		i <- i + 1;
	FinMientras
	
	// Si ninguno de los dos ha ganado pero YA NO hay casillas disponibles, entonces el juego termina en empate.
	// Los espacios disponibles estan representados con un espacio
    // Al inicio de la iteracion ya asignamos ganador a "Empate". Si para este punto ninguna condicion se
	// cumplio, entonces eso sera devuelto. De lo contrario, alguna de las demas condiciones se habra devuelto en su lugar.
FinFuncion


// El juego
Algoritmo TicTacToe
	// Definimos algunas variables
	Definir movimiento como Cadena;
	Definir fila, columna como Entero;
	
    // Inicializamos un tablero vacio
    Definir posiciones como Cadena;
	Dimension posiciones(9);
	
	// Lo llenamos con espacios para representar las casillas vacias
	Definir i como Entero;
	Para i<-1 Hasta 9 Hacer
		posiciones[i] <- " ";
	FinPara

    // Representaremos el turno actual con un valor booleano,
    // donde Verdadero representa el turno de las X y Falso el de las O
    Definir turno_X como Logico;
	turno_X <- Verdadero;

    LimpiarPantalla
	
	Definir ganador, jugador como Cadena;
    ganador <- "Nadie";


    // Mainloop del juego
    Mientras ganador = "Nadie" Hacer
		Si turno_X Entonces
			jugador <- "X";
		SiNo
			jugador <- "O";
		FinSi

        // Imprimimos la UI
        ImprimirTablero(posiciones);

        // Verificamos si hay algun ganador de la iteracion anterior del loop
        ganador <- ComprobarGanador(posiciones);
		
        Si ganador = "Nadie" Entonces
            // Le solicitamos el input al usuario
			Escribir "";	// \n
            Escribir "Turno del jugador ", jugador, ". Elige una posicion (1-3, 1-3): ";
			Leer movimiento;

			// Sanitizamos un poquito el input
			movimiento <- Remplazar(movimiento, " ", "");	// Removemos espacios en blanco
			
			// Este programa ignorara los excesos (osea, poner una coordenada de mas de 2 elementos como x,yyy,zzz).
			// Este programa no va a atrapar casos donde el usuario ingrese valores no numericos o
			// coordenadas rotas (Osea, cualquier cosa que no sea (x,y) con espacios en blanco).
			// Significa que tampoco atrapara casos en los que el usuario ingrese coordenadas de mas de 1 digito.
			// Jesucristo sabe que no pienso matarme sanitizando el input en pseudocodigo de PSeInt.
			Escribir movimiento;
			fila <- ConvertirANumero(Subcadena(movimiento, 1, 1));
			columna <- ConvertirANumero(Subcadena(movimiento, 3, 3));

            // Verificamos si las coordenadas ingresadas son validas (estan entre 1 y 3)
			// Esto ya es demasiado pedir dios santo odio pseudocodigo no puedo ni poner acentos.
			Si NO (1 <= fila Y fila <= 3) O NO (1 <= columna Y columna <= 3) Entonces
                // El jugador introdujo coordenadas o muy chiquitas o muy grandes.
                // Le pedimos que las introduzca de nuevo sin saltarnos su turno.
                LimpiarPantalla
                Escribir "[!] Las coordenadas que ha ingresado son invalidas. Por favor, intente de nuevo.";
				Escribir "";	// \n
			SiNo
				// Verificamos si la casilla ya estaba ocupada
				Si posiciones[Coordenadas(fila, columna, 3)] <> " " Entonces
					// El jugador ha tratado de jugar en una casilla ya usada.
					// Le avisamos y le pedimos que introduzca otra distinta,
					// pero no nos saltamos su turno.
					LimpiarPantalla
					Escribir "[!] La casilla que ha introducido ya esta usada. Por favor, escoga otra.";
					Escribir "";	// \n
                SiNo
					// Insertamos el movimiento del jugador en las posiciones
					posiciones[Coordenadas(fila, columna, 3)] <- jugador;
					
					// Invertimos el valor de verdad de la variable que rastrea el turno
					// para pasarle el turno al jugador opuesto al actual.
					turno_X <- NO turno_X;
					
					LimpiarPantalla
				FinSi
			FinSi
		FinSi
	FinMientras
	
	// El juego ha terminado. Verificamos el ganador
	// Coloco este chequeo al final del juego despues del loop para que no se tenga
	// que revisar en cada iteracion, sino 1 sola vez al final de la partida.
	Si ganador <> "Empate" Entonces
		Escribir "";	// \n
		Escribir "¡El jugador ", ganador, " ha ganado!";
	SiNo
		Escribir "";	// \n
		Escribir "¡El juego ha terminado en empate!";
	FinSi
FinAlgoritmo

// Odio pseudocodigo. Esto fue espantoso.
// No habia excusa para complicarme de esta forma

