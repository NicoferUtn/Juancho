

# Ejercicio 11: Realizar un programa que lea un número natural H e imprima un mensaje indicando si H es primo o no. 
# Se dice que un número es primo cuando sólo es divisible por sí mismo y por la unidad.


Numero = int(input("Decime un numero: "))

while Numero <= 1: #Pido numeros hasta que sean mayor a 1 
    print("El número debe ser mayor que 1. Intentalo de nuevo.")
    Numero = int(input("Decime qué número querés verificar si es primo: "))

#La condicion que el Numero % Numero == 0 la cumplen todos asique pajona

Divisor = 2
esPrimo = 1
while Divisor < Numero : #Descarto el caso del 1 y el de Numero % Numero == 0 por eso la condicion de (Divisor < Numero)
    if Numero % Divisor == 0:
        esPrimo = -1 # Es lo mimso que usar True y false solo que mas feo JEJE 
    Divisor += 1

if esPrimo == 1:
    print("El numero ", Numero,"ES PRIMO")
else:
    print("El numero ", Numero,"NO ES PRIMO")


