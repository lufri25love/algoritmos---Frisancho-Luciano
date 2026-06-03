"""
2. Realizar un programa que pida la carga de dos listas numéricas enteras
de 4 elementos cada una. Generar una tercera lista que surja de la suma
de los elementos de la misma posición de cada lista. Mostrar esta tercera
lista.
"""

lista1 = []
lista2 = []
lista3 = []

print("carga de la primera lista con numeros")
for x in range(4):
    num = int(input(f"ingrese un numero para la posicion "))
    lista1.append(num)

print("\ncarga de la segunbda lista con numeros ")
for x in range(4):
    num = int(input(f"ingrese un numero para la posicion "))
    lista2.append(num)

for x in range(4):
    suma = lista1[x] + lista2[x]
    lista3.append(suma)

print("\nprimera lista : ", lista1)
print("segunda lista ", lista2)
print("tercera lista (sumas) : " , lista3)