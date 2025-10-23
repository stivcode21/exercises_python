#1 === arreglo con 5 nombres y mostrar cada uno en pantalla ===

nombres = []

for i in range(1, 6):
    nombre = input(f"nombre {i}:")
    nombres.append(nombre)

print("\nLISTA DE NOMBRES:")
for nombre in nombres:
    print(nombre)