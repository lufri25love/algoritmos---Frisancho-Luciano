"""
1. Se desea desarrollar un programa que permita registrar los nombres y las
calificaciones de 6 estudiantes. Luego de cargar los datos, se debe mostrar el
nombre del estudiante con la nota más alta, junto con su nota. Al igual que el
estudiante con la nota más baja. Informar si hay estudiantes con la misma nota
máxima o mínima.
"""

nombres=[]
calificaciones=[]

for x in range(6):
    nom=input(f"ingrese el nombre del estudiante ")
    nombres.append(nom)
    cal=input(f"ingrese la calificacion de {nom} ")
    calificaciones.append(cal)

mayor=calificaciones[0]
posicion=0
for x in range(1,6):
    if calificaciones[x]>mayor:
        mayor=calificaciones[x]
        posicion=x

menor=calificaciones[0]
posicio=0
for x in range(1,6):
    if calificaciones[x]<menor:
        menor=calificaciones[x]
        posicio=x


print(f"el alumno {nombres[posicion]} tiene la mayor nota que es {mayor} ")
print(f"el alumno {nombres[posicio]} tiene la menor nota que es {menor} ")