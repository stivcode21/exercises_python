#1 === arreglo con 5 nombres y mostrar cada uno en pantalla ===

# Nombres = []

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

#4 === guardar 10 numero en un arreglo y mostrar solo los pares ===

# numeros = [14, 11, 45, 36, 25, 20, 80, 13, 50, 40]
# pares = []

# for numero in numeros:
#     isPar = numero % 2
#     if isPar == 0:
#         pares.append(numero)

# print("\n NUMEROS PARES:")
# for par in pares:
#     print(par)

#5 === leer 5 nombres y luego busque si el nombre ingresado esta en la lista ===

# listaDeNombres = []

# for i in range(1, 6):
#     nombre = input(f"Nombre {i}:")
#     listaDeNombres.append(nombre)

# buscarNombre = input("\nIngresa nombre a buscar: ")

# if buscarNombre in listaDeNombres:
#     print("Nombre encontrado")
# else:
#     print("Nombre no fue encontrado")

#6 === ingresar 8 notas y mostrar la mas alta y la mas baja ===

# notas = []

# for i in range(1, 9):
#     nota = float(input(f"ingresa nota {i}:"))
#     notas.append(nota)

# notaMayor = max(notas)
# notaMenor = min(notas)

# print(f"Nota mayor: {notaMayor}\nNota menor: {notaMenor}")

#7 === pedir 10 numeros y luego ordenar de mayor a menor ===

numeros = []

for i in range(1, 11):
    numero = int(input(f"ingresa numero {i}:"))
    numeros.append(numero)

numeros.sort()

print(f"numero ordenados\n{numeros}")