import random

equipos = []
tabla = [] 

print("⚽ INGRESA LOS 4 EQUIPOS\n")
for i in range(1, 5):
    nombre = input(f"ingresa nombre de equipo {i}: ")

    equipo = {
        "nombre": nombre,
        "puntos": 0
    }

    equipos.append(equipo)

#simulacion de enfrentamientos por puntos
for i in range(1, 4):
    for equipo in equipos:
        numero = random.randint(0, 3)
        equipo["puntos"] += numero

tabla = sorted(equipos, key=lambda equipo: equipo["puntos"], reverse=True)

print("📜 TABLA DE POSICIONES")
for equipo in tabla:
    print(f"=== EQUIPO: {equipo["nombre"]} -- PUNTOS={equipo["puntos"]} ===")