"""
4. Crear dos listas paralelas. En la primera ingresar los nombres de empleados y
en la segunda los sueldos de cada empleado.
Ingresar por teclado cuando inicia el programa la cantidad de empleados de la
empresa.
Borrar luego todos los empleados que tienen un sueldo mayor a 10000 (tanto el
sueldo como su nombre)
"""
empleados=[]
sueldos=[]
kiki=int(input("¿Cuantos empleados queres ingresar?"))
for x in range(kiki):
    n=input(f"Ingrese el nombre del empleado {x+1}: ")
    empleados.append(n)
    s=int(input(f"Ingrese el sueldo de {n}: "))
    sueldos.append(s)
for x in range(kiki):
    print(f"{empleados[x], sueldos[x]}")
posicion=0
while posicion < len(sueldos):
    if sueldos[posicion] > 10000:
        sueldos.pop(posicion)    # borramos el sueldo
        empleados.pop(posicion)  # borramos el nombre en la misma posición
    else:
        posicion = posicion + 1  # solo avanzamos si NO borramos

print("Empleados con sueldo menor o igual a 10000 ")
for x in range(len(empleados)):
    print(f"{empleados[x]}: {sueldos[x]}")