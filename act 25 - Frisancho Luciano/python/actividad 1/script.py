"""1-
Confeccionar un programa que permita registrar las temperaturas máximas de las últimas
6 horas en una lista.
Desarrollar las siguientes funciones:
1. Carga: Solicitar al operador el ingreso por teclado de las 6 temperaturas y
almacenarlas en una lista.
2. Procesar Extremos: Recibir la lista como parámetro y retornar una tupla que
contenga en su primer componente el valor máximo y en el segundo el valor
mínimo.
3. Bloque Principal: Desempaquetar la tupla devuelta por la función anterior en dos
variables individuales (máxima y mínima) y mostrarlas en pantalla con un mensaje
descriptivo."""

def cargar_temperaturas():
    lista=[]
    for x in range(6):
        tem=int(input(f"ingrese la temperatura n°{x+1} de las ultimas 6 horas : "))
        lista.append(tem)
    return lista

def mayor_y_menor(lista):
    men=lista[0]
    may=lista[0]
    for elemento in lista:
        if elemento>may:
            may=elemento
        elif elemento<men:
            men=elemento
    return (may,men)

def imprimir(tuplas):
    print("---la mayor y menor temperatura de las ultimas 6 horas---")
    may, men = tuplas
    print("el valor mayor de las temperaturas es : ", may)
    print("el valor menor de las temperaturas es : ", men)

#bloque principal
lista=cargar_temperaturas()
mayor_y_menor(lista)
imprimir(mayor_y_menor(lista))
