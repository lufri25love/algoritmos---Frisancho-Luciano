"""
3. Se registran los nombres de 5 atletas y sus tiempos (en segundos) en una
carrera de 100 metros. El programa debe cargar los datos en dos vectores
paralelos, calcular y mostrar el promedio de los tiempos, mostrar el nombre del
atleta con mejor y peor tiempo, y mostrar los nombres de quienes superaron el
promedio.
"""
nombres=[]
tiempo=[]
suma_tiempos=0

for x in range(5):
    nom=input(f"ingrese el nombre del atleta ")
    nombres.append(nom)
    cal=float(input(f"ingrese el tiempo de carrera de 100 metros de {nom} "))
    tiempo.append(cal)
for x in range(5):
    suma_tiempos=suma_tiempos+tiempo[x]
    promedio=suma_tiempos/5
    
mayor=tiempo[0]
posicion=0
for x in range(1,5):
    if tiempo[x]<mayor:
        mayor=tiempo[x]
        posicion=x

menor=tiempo[0]
posicio=0
for x in range(1,5):
    if tiempo[x]>menor:
        menor=tiempo[x]
        posicio=x

print("PROMEDIO")
print(f"el promedio de los atletas es {promedio}")
print(f"el atleta {nombres[posicion]} tiene el mejor tiempo de carrera que es {mayor} ")
print(f"el atleta {nombres[posicio]} tiene el peor tiempo de carrera que es {menor}  ")

print("atletas que superaron el promedio de carrera")
for j in range(5):
    if tiempo[j]<=promedio:
        print(nombres[j])


