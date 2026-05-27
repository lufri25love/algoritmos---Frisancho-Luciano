#3. Realizar un programa que solicite la carga por teclado de dos números, si el
#primero es mayor al segundo informar su suma y diferencia, en caso
#contrario informar el producto y la división del primero respecto al segundo.
num1 = int(input("ingrese el primer numero valor: "))
num2 = int(input("ingrese el segundo numero valor: "))
suma=num1+num2
diferencia=num1-num2
multi=num1+num2
division=num1/num2
if num1<num2:
    print(f"la suma de los dos numeros es {suma}")
    print(f"la diferencia entre los dos numeros es {diferencia}")
else:
    print(f"la multiplicacion de los productos es {multi}")
    print(f"la division de los numeros es {division}")



