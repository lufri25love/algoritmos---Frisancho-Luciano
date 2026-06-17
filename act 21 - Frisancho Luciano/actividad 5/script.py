"""
5-
Almacenar los nombres de 5 productos y sus precios. Utilizar una lista y cada
elemento una tupla con el nombre y el precio.
Desarrollar las funciones:
1) Cargar por teclado.
2) Listar los productos y precios.
3) Imprimir los productos con precios comprendidos entre 10 y 15.
"""
def cargar_datos():
    lista=[]
    for x in range(5):
        produ=input("ingrese el nombre del producto : ")
        preci=int(input(f"ingrese el precio de {produ} : "))
        lista.append((produ,preci))
    return lista

def listar(lista):
    print("----lista de productos y precios----")
    listita=list(lista)
    for x in range(5):
        print(listita[x])

def precios_comprendidos(lista):
    print("----productos con precios comprendidos entre 10 y 15----")
    posi=0
    for x in range(5):
        if 10<= lista[x][1] <=15:
            posi=x
            print(f"producto {lista[posi][0]} con precio de {lista[posi][1]}")
            

lista=cargar_datos()
listar(lista)
precios_comprendidos(lista)
