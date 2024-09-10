

# Ejercicio 9: Se desea analizar cuántos autos circulan con patente con numeración par y 
# cuántos con numeración impar en un día. Escribir un programa que permita ingresar la terminación de la patente (entre 0 y 9) hasta ingresar -1 e informe 
# cuántos vehículos pasaron con numeración par y cuántos con numeración impar.

NumeroPatente = 0
PatetnetePar = 0
PatenteImpar = 0

while NumeroPatente != -1 : 
    NumeroPatente = int(input("Decime la terminacion de la patente: "))

    if NumeroPatente % 2 == 0 :
        PatetnetePar += 1
        
    elif NumeroPatente % 2 != 0 and NumeroPatente != -1 : #Uso del and para decir que Si o Si se deben cumplor esas 2 condiciones 
        PatenteImpar += 1

# Muesto por pantalla los las patentes pares e impares
print("La Cantidad de patentes PARES: ", PatetnetePar)
print("La Cantidad de patentes IMPARES: ", PatenteImpar)
    