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

estudiantes = [
    {"nombre": "juanito", "nota": 4.5},
    {"nombre": "carlos", "nota": 3.5},
    {"nombre": "maria", "nota": 3.0},
    ]

for estudiante in estudiantes:
    nota = estudiante["nota"]

    if nota >= 3.5:
        nombreEstudiante = estudiante["nombre"]
        print(nombreEstudiante)