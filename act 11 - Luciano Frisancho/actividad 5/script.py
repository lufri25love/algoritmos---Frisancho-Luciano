#5. Se ingresa por teclado un valor entero, mostrar una leyenda que indique si
#el número es positivo, negativo o nulo (es decir cero)
num1 = int(input("ingrese un numero: "))
if num1 > 0:
    print("su numero es positivo")
elif num1 < 0:
    print("su numero es negativo")
else:
    print("su numero es nulo")