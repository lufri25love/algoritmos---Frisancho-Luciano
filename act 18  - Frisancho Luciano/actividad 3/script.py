"""
3. Confeccionar una función que calcule la superficie de un rectángulo y la
retorne, la función recibe como parámetros los valores de dos de sus lados:
def retornar_superficie(lado1,lado2):
En el bloque principal del programa cargar los lados de dos rectángulos y
luego mostrar cuál de los dos tiene una superficie mayor.
"""

def cargar_valor():
    valor1=int(input("ingrese el primer valor del primer rectangulo : "))
    valor2=int(input("ingrese el segundo valor del primer rectangulo : "))
    valor3=int(input("ingrese el primer valor del segundo rectangulo : "))
    valor4=int(input("ingrese el segundo valor del segundo rectangulo : ")) 
    multi1=valor1*valor2
    multi2=valor3*valor4
    print("la superficie del primer rectangulo es :" , multi1)
    print("la superficie del segundo rectangulo es :" , multi2)
    print(f"el mayor de los rectangulos es : ", retornar_mayor(multi1,multi2))

def retornar_mayor(v1,v2):
    if v1>v2:
        mayor=v1
    else:
        mayor=v2
    return mayor
    

cargar_valor()
