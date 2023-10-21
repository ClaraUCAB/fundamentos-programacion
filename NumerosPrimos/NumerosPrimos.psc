// Programa para calcular si un n�mero es primo o no
Proceso NumerosPrimos
    // Definimos las variables para operar
    Definir num, i como Entero;
	Definir primo como Logico;
	
	primo <- Verdadero;

    // Le solicitamos un n�mero entero al usuario
    Escribir "Por favor, ingrese un numero: ";
    Leer num;

    // Primero podemos descartar todos los n�meros que no sean mayores a 1
    Si !(num > 1)
        primo <- Falso;
	SiNo
		// Ahora podemos iterar entre todos los n�meros del 2 hasta la ra�z cuadrada del n�mero.
		// Es suficiente llegar hasta la ra�z y no el rango completo ya que tratando de encontrar
		// factores que dividan al n�mero del usuario, n�meros m�s all� de su ra�z no pueden multiplicarse
		// para componer al n�mero exacto, y por lo tanto podemos descartarlos autom�ticamente.
		// De esta forma nos ahorramos una cantidad gigantezca de ciclos y nuestro programa es m�s eficiente.
		// Si ninguno de los n�meros del 2 a su ra�z es factor suyo, eso solo deja a 1 y a s� mismo como factores,
		// lo que significa que s� es primo, y si s� hay alg�n factor adem�s de 1 y s� mismo, entonces no es primo.
		
		// Con esto podemos iterar hasta la ra�z del n�mero del usuario
		i <- 2;
		Mientras i*i <= num
			// Comprobamos si el n�mero es divisible entre i o no
			// Si es divisible, entonces no es primo
			Si num % i == 0
				primo <- Falso;
				i <- num;	// Esto har� que la siguiente iteraci�n del ciclo sea falsa, termin�ndolo
			FinSi
			
			i <- i + 1;
		FinMientras
	FinSi
	
	// Imprimimos el resultado
	Si primo
		Escribir "El numero ", num, " si es primo.";
	SiNo
		Escribir "El numero ", num, " no es primo.";
	FinSi
FinProceso
