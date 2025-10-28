#TALLER DICCIONARIOS

#1 Diccionario de persona

persona = {
    "nombre": "juanito",
    "edad": "29",
    "ciudad": "manizales"
}

print(persona["nombre"])
print(persona.get("edad"))

#2 acceder y modificar valores

persona["ciudad"] = "medellin"
persona["profesion"] = "arquitecto" 

print(persona)

#3 contar claves

totalClaves = len(persona)
print(totalClaves)