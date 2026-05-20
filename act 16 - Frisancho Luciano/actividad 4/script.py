"""
4. Se realiza una evaluación a 6 docentes por parte de sus alumnos. Se registran
sus nombres y puntajes promedio obtenidos (de 1 a 10).
Cargar sus datos en vectores paralelos, mostrar docente con calificación más
alta y más baja, ordenar los vectores de mayor a menor de acuerdo con la
calificación y mostrar en pantalla la cantidad de docentes que aprobaron y
desaprobaron (tomando como base que se aprueba con una nota mayor o
igual a 6)
"""

nombres=[]
puntaje=[]

for x in range(6):
    nom=input(f"ingrese el nombre del docente ")
    nombres.append(nom)
    cal=float(input(f"ingrese el promedio del 1 al 10 que tuvo el docente {nom} "))
    puntaje.append(cal)


mayor=puntaje[0]
posicion=0
for x in range(1,6):
    if puntaje[x]>mayor:
        mayor=puntaje[x]
        posicion=x

menor=puntaje[0]
posicio=0
for x in range(1,6):
    if puntaje[x]<menor:
        menor=puntaje[x]
        posicio=x

print(f"el docente {nombres[posicion]} tiene el mayor puntaje que es {mayor} ")
print(f"el docente {nombres[posicio]} tiene el menor puntaje que es {menor} ")
print("docentes que aprobaron por tener puntaje mayor a 6 o igual")
for i in range(6):
    if puntaje[i]>=6:
        print(nombres[i])

print("docentes que desaprobaron por tener puntaje menor a 6")
for o in range(6):
    if puntaje[o]<6:
        print(nombres[o])


