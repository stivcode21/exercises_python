#8 Contar vocales en una letra
palabra = input("ingresa una palabra: ")
contador = 0
vocales = ["a","e","i","o","u"]

for letra in palabra:
    if letra in vocales:
        contador = contador + 1

if contador == 0:
    print("tu palabra no tiene vocales")
else:
    print("Numero total de vocales de tu palabra es: ", contador)