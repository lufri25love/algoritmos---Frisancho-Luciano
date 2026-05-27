#2) Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio de las personas.

promedio = 0

n = int(input("Ingrese cuántas alturas va a ingresar: "))

for x in range(1, n+1):
    altura = int(input(f"Ingresar la altura de la persona {x}: "))
    promedio += altura
    promedio = promedio / n

print("La altura promedio es: ", promedio)