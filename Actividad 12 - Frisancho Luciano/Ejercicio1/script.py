#1) Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.

cantMenor7=0
cantMayor7=0

for x in range(1,11):
    nota = int(input(f"Ingrese la nota del alumno {x}: "))

    if nota<7:
        cantMenor7 = cantMenor7 + 1

    elif nota>=7:
        cantMayor7 = cantMayor7 + 1

print("La cantidad de alumnos con nota menor a 7 son: ", cantMenor7)
print("La cantidad de alumnos con nota mayor o igual a 7 son: ", cantMayor7)