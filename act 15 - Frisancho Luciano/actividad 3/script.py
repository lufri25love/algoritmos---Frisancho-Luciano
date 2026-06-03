"""
3. Solicitar por teclado la cantidad de empleados que tiene la empresa. Crear
y cargar una lista con todos los sueldos de dichos empleados. Imprimir la
lista de sueldos ordenamos de menor a mayor.
"""

sueldos = []

cantidad= int(input("ingrese la cantidad de empleados de la empresa : "))

for x in range(cantidad):
    sueldo = float(input(f"ingrese el sueldo del empleado : "))
    sueldos.append(sueldo)

for i in range(cantidad):
    for j in range(cantidad - 1):

        if sueldos[j] > sueldos [j + 1]:

            aux = sueldos[j]
            sueldos[j] = sueldos[j + 1]
            sueldos[j + 1] = aux

print("\nlista de sueldo ordenados de menor a mayor : ")
print(sueldos)