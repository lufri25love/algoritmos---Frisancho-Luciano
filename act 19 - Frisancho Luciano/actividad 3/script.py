"""
3. Confeccionar una función que reciba entre 2 y 5 enteros. La misma nos
debe retornar la suma de dichos valores. Debe tener tres parámetros por
defecto.
"""

def cal_suma(a1,a2,a3=0,a4=0,a5=0):
    suma = a1 + a2 + a3 + a4 + a5    
    return suma

def mostra(resultado):
    print("-RESULTADO-")
    print("la suma de dichos valores es : ")
    print(resultado)

print("ingrese datos:")
n1 = int(input("ingrese valor del primer numero : "))
n2 = int(input("ingrese valor del segundo numero : "))
n3 = int(input("ingrese valor del tercer numero : "))

total = cal_suma(n1,n2,n3)

mostra(total)