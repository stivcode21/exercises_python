#TALLER DICCIONARIOS

#1 Diccionario de persona

# persona = {
#     "nombre": "juanito",
#     "edad": "29",
#     "ciudad": "manizales"
# }

# print(persona["nombre"])
# print(persona.get("edad"))

#2 acceder y modificar valores

# persona["ciudad"] = "medellin"
# persona["profesion"] = "arquitecto" 

# print(persona)

#3 contar claves

# totalClaves = len(persona)
# print(totalClaves)

#4 lista de estudiantes

# estudiantes = [
#     {"nombre": "juanito", "nota": 4.5},
#     {"nombre": "carlos", "nota": 3.5},
#     {"nombre": "maria", "nota": 3.0},
#     ]

# for estudiante in estudiantes:
#     nota = estudiante["nota"]

#     if nota >= 3.5:
#         nombreEstudiante = estudiante["nombre"]
#         print(nombreEstudiante)

#5 contar ocurrencias

# frase = input("Ingresa un frase aleatoria: ")

# palabras = frase.split()

# for palabra in set(palabras):
#     counter = palabras.count(palabra)
#     print(f"la palabra '{palabra}' aparece = {counter}")

#6 mejor calificacion

# notas = {"Ana": 3.8, "Carlos": 4.5, "Luisa": 4.0}

# mayorNota = max(notas, key=notas.get)

# print("El estudiante con la mayor nota es:", mayorNota)
# print("Su nota es:", notas[mayorNota])

#7 inventario de productos

# inventario = {
#     "pera": {"precio": 1000, "cantidad": 10},
#     "mango": {"precio": 2000, "cantidad": 15},
#     "manzana": {"precio": 1000, "cantidad": 25},
#     "sapote": {"precio": 1500, "cantidad": 15},
#     "piña": {"precio": 3500, "cantidad": 5}
# }

# inventarioTotal = 0

# for fruta in inventario.values():
#     precioFruta = fruta["precio"]
#     cantidadFruta = fruta["cantidad"]

#     subtotal = precioFruta * cantidadFruta
#     inventarioTotal += subtotal

# print(f"Precio total del inventario es: {inventarioTotal}")

#8 conversion de lista a diccionario

claves = ["nombre", "edad", "curso"]
valores = ["Jouler", 25, "Python"]

persona = {}

for i in range(0, 3):
    persona[claves[i]] = valores[i]

print(persona)