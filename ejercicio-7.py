#7 Tabla de multiplicar
numero = int(input("escribe un numero: "))
multiplicador = 0

while multiplicador <= 10:
    resultado = numero * multiplicador
    print( numero," x ", multiplicador," = ", resultado)
    multiplicador = multiplicador + 1