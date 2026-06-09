"""
1. Crear una lista de enteros por asignación. Definir una función que reciba
una lista de enteros y un segundo parámetro de tipo entero. Dentro de la
función mostrar cada elemento de la lista multiplicado por el valor entero
enviado.
lista=[3, 7, 8, 10, 2]
multiplicar(lista,3)
"""
listaN=[]

def multiplicarizar(lista):
    multi=lista[0]
    for x in range(len(lista)):
        multi=3*lista[x]
        listaN.append(multi)
    return listaN



listavalores=[3, 7, 8, 10, 2]
print("la list completa es : ")
print(listavalores)
print("la multiplicacion de cada valor de la lista es : ")
print(multiplicarizar(listavalores))