
# Ejercicio 8: Ingresar números, hasta que la suma de los números pares supere 100. Mostrar 
# cuántos números se ingresaron en total.

SumatoriaDeNumeros = 0
CantidadDeNumeros = 0

while SumatoriaDeNumeros < 100 :
    numero = int(input("Decime un numero para sumar: "))
    
    if numero % 2 == 0 : #Reviso si el numero es par eso se hace si el resto de dividir por 2 es 0 
        SumatoriaDeNumeros += numero
    
    CantidadDeNumeros += 1 # Contador de numeros Utilizados 
    

print("La Cantidad de numeros utilizados fueron: ", CantidadDeNumeros)
