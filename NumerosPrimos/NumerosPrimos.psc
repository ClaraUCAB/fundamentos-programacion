// Programa para calcular si un numero es primo o no
Proceso NumerosPrimos
    // Definimos las variables para operar
    Definir num, i como Entero;
	Definir primo como Logico;
	
	primo <- Verdadero;

    // Le solicitamos un numero entero al usuario
    Escribir "Por favor, ingrese un numero: ";
    Leer num;

    // Primero podemos descartar todos los numeros que no sean mayores a 1
    Si !(num > 1)
        primo <- Falso;
	SiNo
		// Ahora podemos iterar entre todos los numeros del 2 hasta la raiz cuadrada del numero.
		// Es suficiente llegar hasta la raiz y no el rango completo ya que tratando de encontrar
		// factores que dividan al numero del usuario, numeros mas alla de su raiz no pueden multiplicarse
		// para componer al numero exacto, y por lo tanto podemos descartarlos automaticamente.
		// De esta forma nos ahorramos una cantidad gigantezca de ciclos y nuestro programa es mas eficiente.
		// Si ninguno de los numeros del 2 a su raiz es factor suyo, eso solo deja a 1 y a si mismo como factores,
		// lo que significa que si es primo, y si si hay algun factor ademas de 1 y si mismo, entonces no es primo.
		
		// Con esto podemos iterar hasta la raiz del numero del usuario
		i <- 2;
		Mientras i*i <= num
			// Comprobamos si el numero es divisible entre i o no
			// Si es divisible, entonces no es primo
			Si num % i == 0
				primo <- Falso;
				i <- num;	// Esto hara que la siguiente iteracion del ciclo sea falsa, terminandolo
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

