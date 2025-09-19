#10 Promedio de alturas
total_altura = 0
contadorDePersonas = 0
miAltura = int(input("INGRESA TU ALTURA: "))

for i in range(1, 6):
    altura = int(input(f"Ingresa altura de la persona {i}: "))
    if altura > miAltura:
        contadorDePersonas += 1

    total_altura += altura

promedio = total_altura / 5
print(f"El promedio de altura es: {promedio} Personas por encima de tu estatura: {contadorDePersonas}")