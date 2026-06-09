"""
4. Elaborar una función que muestre la tabla de multiplicar del valor que le
enviemos como parámetro. Definir un segundo parámetro llamado termino
que por defecto almacene el valor 10. Se deben mostrar tantos términos de
la tabla de multiplicar como lo indica el segundo parámetro.
Llamar a la función desde el bloque principal de nuestro programa con
argumentos nombrados.
"""

def multi(ar):
    for x in range(1,11):
        print(f"{ar} x {x} = {ar*x}")
    
def mostrar(ar):
    print("RESULTADO")
    multi(ar)

def valores():
    print("INGRESE LOS DATOS")
    ar=int(input("ingrese el valor del numero : "))
    return ar

numero = valores()
mostrar(numero)