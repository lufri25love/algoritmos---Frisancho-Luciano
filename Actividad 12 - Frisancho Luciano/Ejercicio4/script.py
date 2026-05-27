#4) Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
#   a. La cantidad de valores ingresados negativos.
#   b. La cantidad de valores ingresados positivos.
#   c. La cantidad de múltiplos de 15.
#   d. El valor acumulado de los números ingresados que son pares.

negativos = 0
positivos = 0
multiplos = 0
pares = 0

for x in range(1,11):
    valores = int(input(f"Ingrese el valor número {x}: "))

    if valores<0:
        negativos = negativos + 1
    
    elif valores>0:
        positivos = positivos + 1
    
    if valores%15==0:
        multiplos = multiplos + 1 
    
    if valores%2==0:
        pares = pares + 1

print("La cantidad de valores negativos son: ", negativos)
print("La cantidad de valores positivos son: ", positivos)
print("La cantidad de valores multiplos de 15: ", multiplos)
print("La cantidad de valores pares son: ", pares)