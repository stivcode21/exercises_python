#6 Numero par o impar
numero = int(input("ingresa un numero: "))
residuo = numero % 2
if residuo == 0:
    print("numero es par")
else:
    print("numero es inpar")