"""
2. Una empresa registra los nombres de sus 5 vendedores y el total de ventas
realizadas por cada uno en un mes. Cargar los nombres y ventas en dos
vectores paralelos, ordenar los datos de mayor a menor según las ventas,
imprimir la lista ordenada con nombre y monto de la venta, e informar quien fue
el que menos vendió de los 5 empleados.
"""

vendedores=[]
ventas=[]

for x in range(5):
    nom=input(f"ingrese el nombre del vendedor ")
    vendedores.append(nom)
    ven=input(f"ingrese el total de las ventas de {nom} en un mes ")
    ventas.append(ven)

for k in range(4):
    for x in range(4):
        if ventas[x]<ventas[x+1]:
            aux1=ventas[x]
            ventas[x]=ventas[x+1]
            ventas[x+1]=aux1
            aux2=vendedores[x]
            vendedores[x]=vendedores[x+1]
            vendedores[x+1]=aux2


menor=ventas[0]
posicio=0
for x in range(1,5):
    if ventas[x]<menor:
        menor=ventas[x]
        posicio=x

print("lista de vendedores y sus ventas ordenadas segun sus ventas")
for x in range(5):
    print(vendedores[x],ventas[x])

print(f"el vendedor {vendedores[posicio]} tiene la menor venta del mes con  {menor} de ventas ")