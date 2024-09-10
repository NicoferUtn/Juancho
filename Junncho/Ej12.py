# Ejercicio 12: La sucesión de Fibonacci es una sucesión de números enteros donde cada término se obtiene como suma de los dos anteriores, siendo los dos primeros 0 y 1. 
# Por lo tanto, Fib=0, 1, 1, 2, 3, 5, 8, 13, 21.... Realizar un programa que lea N e 
# imprima los N primeros términos de esta sucesión, como así también la suma de 
# los mismos

Numero = int(input("Hata que Punto hay que hacer la sucesion de fibonacci: "))

# Validamos que Numero sea un número mayor o igual a 1
while Numero <= 0:
    print("El número debe ser mayor que 0. Intentalo de nuevo.")
    Numero = int(input("Hata que Punto hay que hacer la sucesion de fibonacci: "))

# Inicializamos los dos primeros términos de la sucesión
fibonacci_1 = 0
fibonacci_2 = 1
contador = 1

# Bucle while para generar la sucesión
if Numero == 1:
    print("Sucesión de Fibonacci con", Numero, "término:", fibonacci_1)
else:
    print("Sucesión de Fibonacci con", Numero, "término:")
    print(fibonacci_1)

    while contador < Numero :  # Ya printeados los casos bases
        fibonacci_siguiente = fibonacci_1 + fibonacci_2
        print(fibonacci_siguiente)
        
        # Actualizamos los valores para la próxima iteración
        fibonacci_1 = fibonacci_2
        fibonacci_2 = fibonacci_siguiente
        
        contador += 1