"""
1-
Confeccionar un programa con las siguientes funciones:
1)Cargar una lista de 5 enteros.
2)Retornar el mayor y menor valor de la lista mediante una tupla.
Desempaquetar la tupla en el bloque principal y mostrar el mayor y menor.
"""
def cargar_datos():
    lista=[]
    for x in range(5):
        li=input("ingrese un  valor entero : ")
        lista.append(li)
    return lista

def mayor_menor(lista):
    may=lista[0]
    men=lista[0]
    for elemento in lista:
        if elemento>may:
            may=elemento
    for element in lista:
        if element<men:
            men=element
    return (may , men)
    


def imprimir(tuplas):
    may, men = tuplas
    print("el valor mayor es : " , may)
    print("el valor mayor es : " , men)


lista=cargar_datos()
mayor_menor(lista)
imprimir(mayor_menor(lista))