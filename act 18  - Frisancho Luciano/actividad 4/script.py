"""
4. Plantear una función que reciba un string en mayúsculas o minúsculas y
retorne la cantidad de letras "a" o "A".
"""
def largo(cadena):
    return len (cadena)

cuantos=0

texto=input("ingrese un texto : ")
te1=largo(texto)
for x in range(len(texto)):
    if "a" and "A" in texto[x]:
        cuantos=[1+x]
print("la letra a o A aparece en el texto : ", cuantos)
    
