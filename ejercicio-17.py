#1 === arreglo con 5 nombres y mostrar cada uno en pantalla ===

# nombres = []

# for i in range(1, 6):
#     nombre = input(f"nombre {i}:")
#     nombres.append(nombre)

# print("\nLISTA DE NOMBRES:")
# for nombre in nombres:
#     print(nombre)

#2 === ingresa 5 numeros y calcular la suma total ===

numeros = []

for i in range(1, 6):
    valor = int(input(f"numero {i}:"))
    numeros.append(valor)

totalSuma = 0
for numero in numeros:
    totalSuma += numero
    
print(f"\nSuma total: {totalSuma}")