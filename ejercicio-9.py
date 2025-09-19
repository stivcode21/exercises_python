#9 calcular el (IMC) de una persona y un mensaje si esta en el cuadro correcto
peso = int(input("ingresa tu peso: "))
altura = int(input("ingresa tu altura: "))

elevadoAlCuadrado = altura ** 2
imc = peso / elevadoAlCuadrado

if imc <= 0.001850:
    print ("IMC: ", imc, "Bajo de peso")
elif imc > 0.001850 and imc <= 0.002499:
    print ("IMC: ", imc, "Normal de peso")
elif imc >= 0.002500 and imc <= 0.002699:
    print ("IMC: ", imc, "Sobrepeso grado 1")
elif imc >= 0.002700 and imc <= 0.002999:
    print ("IMC: ", imc, "Sobrepeso grado 2")
elif imc >= 0.003000 and imc <= 0.003499:
    print ("IMC: ", imc, "Obesidad tipo 1")
elif imc >= 0.003500 and imc <= 0.003999:
    print ("IMC: ", imc, "Obesidad tipo 2")
else: 
    print("Obesidad de tipo (morbida)")