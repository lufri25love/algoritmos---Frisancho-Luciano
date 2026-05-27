#5) Realizar un programa que lea los lados de n triángulos, e informar:
#    a. De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados
#       iguales), isósceles (dos lados iguales), o escaleno (ningún lado igual)
#    b. Cantidad de triángulos de cada tipo.

n = int(input("¿Cuántos triángulos desea ingresar?: "))

cantEqui = 0
cantIso = 0
CantEsca = 0

for x in range(0, n+1):
    lado1 = int(input("Ingrese el primer lado: "))
    lado2 = int(input("Ingrese el segundo lado: "))
    lado3 = int(input("Ingrese el tercer lado: "))

    if lado1==lado2 and lado2==lado3:
        print("El triángulo es equilátero.")
        cantEqui = cantEqui + 1

    elif lado1==lado2 and lado3!=lado2 or lado1!=lado2 and lado2==lado3 or lado1==lado3 and lado3!=lado2:
        print("El triangulo es isósceles.")
        cantIso = cantIso + 1

    elif lado1!=lado2 and lado2!=lado3:
        print("El triángulo es escaleno.")
        CantEsca = CantEsca + 1

print("Cantidad de triángulos Equiláteros: ", cantEqui)
print("Cantidad de triángulos Isósceles: ", cantIso)
print("Cantidad de triángulos Escalenos: ", CantEsca)