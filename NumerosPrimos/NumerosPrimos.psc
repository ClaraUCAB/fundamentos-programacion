// Programa para calcular si un número es primo o no
Proceso NumerosPrimos
    // Definimos las variables para operar
    Definir num, i como Entero;
	Definir primo como Logico;
	
	primo <- Verdadero;

    // Le solicitamos un número entero al usuario
    Escribir "Por favor, ingrese un numero: ";
    Leer num;

    // Primero podemos descartar todos los números que no sean mayores a 1
    Si !(num > 1)
        primo <- Falso;
	SiNo
		// Ahora podemos iterar entre todos los números del 2 hasta la raíz cuadrada del número.
		// Es suficiente llegar hasta la raíz y no el rango completo ya que tratando de encontrar
		// factores que dividan al número del usuario, números más allá de su raíz no pueden multiplicarse
		// para componer al número exacto, y por lo tanto podemos descartarlos automáticamente.
		// De esta forma nos ahorramos una cantidad gigantezca de ciclos y nuestro programa es más eficiente.
		// Si ninguno de los números del 2 a su raíz es factor suyo, eso solo deja a 1 y a sí mismo como factores,
		// lo que significa que sí es primo, y si sí hay algún factor además de 1 y sí mismo, entonces no es primo.
		
		// Con esto podemos iterar hasta la raíz del número del usuario
		i <- 2;
		Mientras i*i <= num
			// Comprobamos si el número es divisible entre i o no
			// Si es divisible, entonces no es primo
			Si num % i == 0
				primo <- Falso;
				i <- num;	// Esto hará que la siguiente iteración del ciclo sea falsa, terminándolo
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
