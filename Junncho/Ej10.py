
# Ejercicio 10: El factorial de un número entero N mayor que cero se define como el producto 
# de todos los enteros X tales que 0 < X <= N. Desarrollar un programa para calcular el factorial de un número dado. Deberán rechazarse las entradas inválidas 


Factorial = int(input("Decime que numero queres que le haga el factorial: "))
    
while Factorial <= 0 : # Pido numeros hasta que sea mayores que 0 
    print("El valor debe ser MAYOR a 0")
    Factorial = int(input("Decime que numero queres que le haga el factorial: "))

TotalDelFactorial = 1
Contador = 1

while Contador <= Factorial:
    TotalDelFactorial *= Contador
    Contador += 1

print("El Valor del factorial es: ", TotalDelFactorial)