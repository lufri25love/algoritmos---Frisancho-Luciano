"""
4-
Se tiene que cargar los votos obtenidos por tres candidatos a una elección.
En una lista cargar en el primer componente el nombre del candidato y en la
segunda componente cargar una lista con componentes de tipo tupla con el
nombre de la provincia y la cantidad de votos obtenidos en dicha provincia.
Se deben cargar los datos por teclado, pero si se cargaran por asignación tendría
una estructura similar a esta:
candidatos=[ (juan,[(cordoba,100),(buenos aires,200)]) , (ana,[(cordoba,55)]) , (luis, [(buenos aires,20)])]
1) Función para cargar todos los candidatos, sus nombres y las provincias con los
votos obtenidos.
2) Imprimir el nombre del candidato y la cantidad total de votos obtenidos en todas
las provincias.
"""
def cargar_valores():
    candidatos=[]
    for x in range(3):
        nom=input("ingrese el nombre del candidato : ")
        pro=input("ingrese el nombre de la provincia : ")
        vot=int(input(f"ingrese la cantidad de votos obtenidos en {pro} : "))
        candidatos.append((nom,pro,vot))
    return candidatos

def imprimir(candidatos):
    print("----lista de candidatos----")
    tupli=tuple(candidatos)
    print(tupli)

candidatos=cargar_valores()
imprimir(candidatos)




