"""
3-
Un equipo de Fórmula 1 registra los nombres de sus 4 pilotos junto con los tiempos (en
segundos) obtenidos en sus últimas 3 vueltas de clasificación.
 La estructura de datos debe ser una lista general. Cada elemento de la lista será
una sublista que contenga en el primer componente el nombre del piloto (cadena
de caracteres) y en el segundo componente una tupla con sus 3 tiempos
(flotantes).
 Sugerencia de estructura interna si se cargara por asignación:
pilotos = [ [Franco, (78.5, 77.2, 79.1)], [Lewis, (77.9, 78.1, 77.4)], ... ]
Desarrollar las siguientes funciones:
1. Cargar pilotos: Solicitar por teclado el nombre de cada uno de los 4 pilotos y sus
3 mejores tiempos para estructurar la lista y las tuplas correspondientes.
2. Calcular Promedios: Recorrer la estructura de datos, calcular el tiempo promedio
de cada piloto en sus 3 vueltas e imprimir su nombre junto a dicho promedio.
3. Mejor Vuelta: Recorrer la estructura para buscar y mostrar la vuelta más rápida de
toda la clasificación (el tiempo individual más bajo dentro de cualquier tupla),
detallando a qué piloto le pertenece.
"""

def cargar_datos():
    pilotos=[]
    for x in range(4):
        nombre=input(f"ingrese el nombre del piloto n°{x+1} : ")
        vue1=float(input(f"ingrese el tiempo de primera ultima vuelta de la calificacion del piloto : "))
        vue2=float(input(f"ingrese el tiempo de segunda ultima vuelta de la calificacion del piloto : "))
        vue3=float(input(f"ingrese el tiempo de tercera ultima vuelta de la calificacion del piloto : "))
        pilotos.append((nombre,vue1,vue2,vue3))
    return pilotos

def promedio_total(pilotos):
    promedio=[]
    for x in range(4):
        suma=pilotos[x][1]+pilotos[x][2]+pilotos[x][3]
        pro=suma/3
        promedio.append(pro)
    return promedio

def imprimir(pilotos,promedio):
    print("------lista de los pilotos y su promedio de tiempo------")
    for x in range(4):
        print(f"el piloto {pilotos[x][0]} tiene un promedio de tiempo de {promedio[x]}")

def mejor(pilotos):
    print("---------------la mejor vuelta------------------")
    mvp=99
    for x in range(4):
        for j in range(3):
            if pilotos[x][j+1]<mvp:
                mvp=pilotos[x][j+1]
                pil=pilotos[x][0]
    print(f"la mejor vuelta fue de {pil},con un tiempo de {mvp}")



pilotos=cargar_datos()
promedio=promedio_total(pilotos)
imprimir(pilotos,promedio)
mejor(pilotos)