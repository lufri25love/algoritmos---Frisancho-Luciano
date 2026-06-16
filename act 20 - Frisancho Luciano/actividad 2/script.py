""""
2. Desarrollar una aplicación que permita ingresar por teclado los nombres de
5 artículos y sus precios.
Definir las siguientes funciones:
1) Cargar los nombres de artículos y sus precios.
2) Imprimir los nombres y precios.
3) Imprimir el nombre de artículo con un precio mayor
4) Ingresar por teclado un importe y luego mostrar todos los artículos con
un precio menor igual al valor ingresado.
"""
def precio_mayor (precio,productos):
    may=precio[0]
    for x in range(1,len(precio)):
        if precio[x]>may:
            may=precio[x]
            posicion=x
    print("----producto con mayor precio---")
    print("el producto :",productos[posicion],"con valor de",may)

def importe(precio,productos):
    porte=int(input("ingrese el importe que tienes : "))
    print("---productos con menor precio o igual precio al importe---")
    for x in range(len(precio)):
        if precio[x]<=porte :
            pocision=x
            print(f"producto : {productos[pocision]} con precio de {precio[x]}")
            
productos=[]
precio=[]
for x in range(5):
    sa=input("ingrese el nombre del producto : ")
    productos.append(sa)
    re=int(input(f"ingrese valor del producto {sa} : "))
    precio.append(re)  
print("---lista de productos y sus respectivos valores---")   
for r in range(5):
    print(f"el nombre del producto es {productos[r]} y su valor es :  {precio[r]} ") 
precio_mayor(precio,productos)
importe(precio,productos)