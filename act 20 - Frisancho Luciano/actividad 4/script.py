"""
4. Confeccionar una función que reciba una serie de edades y me retorne la
cantidad que son mayores o iguales a 18 (como mínimo se envía un entero
a la función)
"""
def personas():
    edades=[]
    for x in range(5):
        cam14=int(input(f"ingrese una edad n°{x+1} : "))
        edades.append(cam14)
    return edades 

def mayores18(edades):
    contador=0
    c=0
    print("---personas mayores de 18 años---")
    for x in range(len(edades)):
        if edades[x]>=18:
            contador+=1
        else:
            c+=1
    print("personas mayores a 18 son : ", contador)
    print("personas menores a 18 son : ", c )
activa_cam=personas()
mayores18(activa_cam)