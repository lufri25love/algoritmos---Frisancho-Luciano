"""
2. En una empresa se almacenaron los sueldos de 10 personas.
Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
1) Carga de los sueldos en una lista.
2) Impresión de todos los sueldos.
3) Cuántos tienen un sueldo superior a $4000.
4) Retornar el promedio de los sueldos.
5) Mostrar todos los sueldos que están por debajo del promedio.
"""

listaMayor=[]

def cargar_datos():
    sue=[]
    for x in range(10):
        s=input("ingrese el sueldo de la persona : " )
        sue.append(s)
    return[sue]
print("----la lista de todos los sueldos----")

def mayores (sueldos):
    print("---los sueldos mayores a 4000---")
    for x in range(len(sueldos)):
        if sueldos[x]>=4000:
            print(sueldos[x])

sueldos=cargar_datos()
mayores(sueldos)