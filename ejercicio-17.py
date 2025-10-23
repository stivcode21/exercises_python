#1 === arreglo con 5 nombres y mostrar cada uno en pantalla ===

# nombres = []

# for i in range(1, 6):
#     nombre = input(f"nombre {i}:")
#     nombres.append(nombre)

# print("\nLISTA DE NOMBRES:")
# for nombre in nombres:
#     print(nombre)

#2 === ingresa 5 numeros y calcular la suma total ===

# numeros = []

# for i in range(1, 6):
#     valor = int(input(f"numero {i}:"))
#     numeros.append(valor)

# totalSuma = 0
# for numero in numeros:
#     totalSuma += numero
    
# print(f"\nSuma total: {totalSuma}")

#3 === leer las edades de 6 personas y sacar el promedio ===

# edades = []
# sumaTotal = 0

# for i in range(1, 7):
#     edad = int(input(f"edad {i}:"))
#     edades.append(edad)

# for edad in edades:
#     sumaTotal += edad

# promedio = sumaTotal / 6
# print(f"Promedio total de edades {promedio}")

#5 === guardar 10 numero en un arreglo y mostrar solo los pares ===

numeros = [14, 11, 45, 36, 25, 20, 80, 13, 50, 40]
pares = []

for numero in numeros:
    isPar = numero % 2
    if isPar == 0:
        pares.append(numero)

print("\n NUMEROS PARES:")
for par in pares:
    print(par)