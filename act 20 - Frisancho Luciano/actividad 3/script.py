"""
3. Confeccionar un programa que permita:
1) Cargar una lista de 10 elementos enteros.
2) Generar dos listas a partir de la primera. En una guardar los valores
positivos y en otra los negativos.
3) Imprimir las dos listas generadas.
"""
def cargar_valor():
    lista=[]
    for z in range(10):
        sakuya=int(input("ingrese numeros positivos o negativos : "))
        lista.append(sakuya)
    return lista

def separar(lista):
    nega=[]
    posi=[]
    for x in range(len(lista)):
        if lista[x] > 0:
            posi.append(lista[x])
        else:
            nega.append(lista[x])
    return nega,posi

def mostri(nega,posi):
    print(posi,nega)


cargar_lista=cargar_valor()
lista1,lista2=separar(cargar_lista)
mostri(lista1,lista2)