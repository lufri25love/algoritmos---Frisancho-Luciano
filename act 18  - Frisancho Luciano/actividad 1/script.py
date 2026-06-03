"""
1. Desarrollar un programa que solicite la carga de tres valores y muestre el
menor. Desde el bloque principal del programa llamar 2 veces a dicha
función (sin utilizar una estructura repetitiva)
"""

def valormenor (valor1,valor2,valor3):
    print ("el valor menor de los 3 numeros es : ")
    if valor1<valor2 and valor1<valor3:
        print(valor1)
    else:
        if valor2<valor3:
            print(valor2)
        else:
            print(valor3)

def cargarvalores():
    valor1= int(input("Ingrese un valor : "))
    valor2= int(input("Ingrese un valor : "))
    valor3= int(input("Ingrese un valor : "))
    valormenor(valor1, valor2, valor3)

cargarvalores()
cargarvalores()