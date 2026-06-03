"""
2. Confeccionar una función que reciba tres enteros y los muestre ordenados
de menor a mayor. En otra función solicitar la carga de 3 enteros por
teclado y proceder a llamar a la primer función definida.
"""


def mostrar_ordenados(valor1, valor2, valor3):
    print("Los números ordenados de menor a mayor son: ")
    
    if valor1 < valor2 and valor1 < valor3:
        if valor2 < valor3:
            print(valor1, valor2, valor3)
        else:
            print(valor1, valor3, valor2)
            
    elif valor2 < valor1 and valor2 < valor3: 
        if valor1 < valor3:
            print(valor2, valor1, valor3)
        else:
            print(valor2, valor3, valor1)
            
    else:
        if valor1 < valor2:
            print(valor3, valor1, valor2)
        else:
            print(valor3, valor2, valor1)

def cargarvalores():
    valor1 = int(input("Ingrese el primer valor: "))
    valor2 = int(input("Ingrese el segundo valor: "))
    valor3 = int(input("Ingrese el tercer valor: "))

    mostrar_ordenados(valor1, valor2, valor3)


cargarvalores()