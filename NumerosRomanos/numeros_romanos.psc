// Programa que convierte numeros romanos a numeros arabigos
Proceso NumerosRomanos
    // Definimos las variables para operar
    Definir romanos como Cadena;
    Definir numeroPrevio, resultado, i como Entero;
	
	// Inicializamos las variables numericas antes de usarlas para evitarnos problemas
	resultado <- 0;
	numeroPrevio <- 0;
	
    // Le solicitamos la entrada en romano al usuario
    Escribir "Ingrese una cifra en numeros romanos: ";
    Leer romanos;
	
    // Convertimos los numeros romanos a mayusculas para
    // no tener que preocuparnos por la capitalizacion
    romanos <- Mayusculas(romanos);
	
    // Evaluamos cada caracter del romano
    Para i<-1 Hasta Longitud(romanos)
		// Lo traducimos a su equivalente arabigo
		Segun SubCadena(romanos, i, i) Hacer
            "I":    // 1
	            resultado <- resultado + 1;
	            numeroPrevio <- 1;
				
            "V":    // 5
                Si numeroPrevio = 1 Entonces
	                // I puede ser usado antes de V para escribir 4.
		            // De esa forma, solo tenemos que sumar 3 para llegar al 4
			        // ya que 1 ya fue sumado en la iteracion anterior que era I.
			        resultado <- resultado + 3;
		        SiNo
			        resultado <- resultado + 5;
				FinSi
			    numeroPrevio <- 5;
				
		    "X":    // 10
		        Si numeroPrevio = 1 Entonces
			        // I puede ser usado antes de X para escribir 9.
				    // De esa forma, solo tenemos que sumar 8 para llegar al 9
                    // ya que 1 ya fue sumado en la iteracion anterior que era I.
                    resultado <- resultado + 8;
                SiNo
                    resultado <- resultado + 10;
				FinSi	
				numeroPrevio <- 10;
				
			"L":    // 50
                Si numeroPrevio = 10 Entonces
                    // X puede ser usado antes de L para escribir 40.
					// De esa forma, solo tenemos que sumar 30 para llegar al 40
					// ya que 10 ya fue sumado en la iteracion anterior que era X.
					resultado <- resultado + 30;
				SiNo
					resultado <- resultado + 50;
				FinSi	
				numeroPrevio <- 50;
				
            "C":    // 100
                Si numeroPrevio = 10 Entonces
                    // X puede ser usado antes de C para escribir 90.
                    // De esa forma, solo tenemos que sumar 80 para llegar al 90
                    // ya que 10 ya fue sumado en la iteracion anterior que era X.
                    resultado <- resultado + 80;
                SiNo
                    resultado <- resultado + 100
                FinSi           
                numeroPrevio <- 100;
				
            "D":    // 500
                Si numeroPrevio = 100 Entonces
                    // C puede ser usado antes de D para escribir 400.
                    // De esa forma, solo tenemos que sumar 300 para llegar al 400
                    // ya que 100 ya fue sumado en la iteracion anterior que era C.
                    resultado <- resultado + 300;
                SiNo
                    resultado <- resultado + 500;
                FinSi                
                numeroPrevio <- 500;
				
            "M":   // 1000
                Si numeroPrevio = 100 Entonces
                    // C puede ser usado antes de M para escribir 900.
                    // De esa forma, solo tenemos que sumar 800 para llegar al 900
                    // ya que 100 ya fue sumado en la iteracion anterior que era C.
                    resultado <- resultado + 800;
                SiNo
                    resultado <- resultado + 1000;
                FinSi                   
                numeroPrevio <- 1000;
				
            De Otro Modo:
                // Si el usuario ha ingresado un caracter invalido,
                // abortamos todas las operaciones y le asignamos
                // al resultado el error para imprimirlo.
				// Esto tambien atrapa el caso en el que el usuario no haya ingresado nada.	
                Escribir "Caracter romano no valido -- ", Subcadena(romanos, i, i);
				resultado <- 0;
				i <- Longitud(romanos);     // Con esto podemos salir del Para
		FinSegun
    FinPara

    // Imprimimos el resultado
	Si resultado > 0 Entonces
		Escribir resultado;
	FinSi
FinProceso
