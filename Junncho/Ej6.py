

# Ejercicio 6: Mostrar la tabla de multiplicar (entre 1 y 12) del número 4. ¿Cómo cambiaría el 
# algoritmo para que el usuario pueda decidir la tabla de multiplicar a mostrar?

NumeroParaTabla = int(input("Decime que numero queres que haha la tabla de multiplicar: ")) #Le pido al usuario que ingrese un numero

numeroActual = 0 #Inicializo la variable numeroActual en 1

while numeroActual <= 12:
    print("Posicion", numeroActual,":",NumeroParaTabla * numeroActual) #Muestro Por pantalla 
    numeroActual += 1 #Le Sumo Para mostrar la siguiente posicion

