#12 Número mayor y menor de 10 numero ingresados
numeros = [] 
for i in range(1, 11):
    numero = int(input(f"ingresa el valor {i}: "))
    numeros.append(numero)

numeromenor = min(numeros)
numeroMayor = max(numeros)
print(f"numero mayor es: {numeroMayor} Numero menor es: {numeromenor}")