"""
4-
Un comercio de tecnología necesita administrar el stock de sus 5 componentes clave de
hardware.
 Crear una lista donde cada elemento sea una tupla de tres elementos que
represente: (nombre_articulo, precio, stock).
Desarrollar las siguientes funciones:
1. Cargar inventario: Ingresar por teclado los datos de los 5 componentes para
armar las tuplas correspondientes.
2. Imprimir listado: Mostrar por pantalla los nombres, precios y stock de todos los
artículos desempaquetando la tupla de manera directa en el bucle for.
3. Valor del Inventario: Calcular e informar el valor total de la mercadería en el local
(sumando el resultado de precio * stock de cada uno de los componentes).
4. Alerta de Reposición: Imprimir el nombre de todos aquellos artículos cuyo stock
sea menor o igual a 10 unidades para emitir un aviso de compra urgente.
"""

def cargar_datos():
    componentes=[]
    for x in range(5):
        nombre=input(f"ingrese el nombre del articulo n°{x+1} : ")
        precio=int(input(f"ingrese el precio del producto {nombre} : "))
        stock=int(input(f"ingrese la cantidad tiene el producto {nombre} : "))
        componentes.append((nombre,precio,stock))
    return componentes

def imrprimir(componentes):                                    
    print("-------------lista de productos con su precio y su stock---------------------")
    for x in range(5):
        print(f"el producto {componentes[x][0]} tiene un precio de {componentes[x][1]} y un stock de {componentes[x][2]} ")

def inventario_total(componentes):
    suma=0
    print("-----------------el monto total de la mercaderia del local-------------------")
    for x in range(5):
        suma=suma+componentes[x][1]*componentes[x][2]
    print(f"el monto total de la mercaderia es de {suma}")

def alerta(componentes):
    print("----------productos con stock menor a 10----------------")
    posi=0
    for x in range(5):
        if componentes[x][2]<=10:       
            posi=x
            print(componentes[posi][0])

#bloque principal
componentes=cargar_datos()
imrprimir(componentes)
inventario_total(componentes)
alerta(componentes)
