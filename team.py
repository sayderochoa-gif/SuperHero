heroes = [
    {"nombre": "Spider-Man", "universo": "Marvel", "poder": "Agilidad", "nivel": 85},
    {"nombre": "Iron Man", "universo": "Marvel", "poder": "Tecnologia", "nivel": 90},
    {"nombre": "Batman", "universo": "DC", "poder": "Inteligencia", "nivel": 88},
    {"nombre": "Superman", "universo": "DC", "poder": "Fuerza", "nivel": 98}
]

grupos = []
total_puntos = 0
dc = []
marvel = []

print("-" * 60)
print("Selecciona tu heroe:")
print("-" * 60)
for i, personaje in enumerate(heroes, start=1):
    print(f"{i}. {personaje['nombre']} ({personaje['universo']})")

for i, personaje in enumerate(heroes, start=1):
    respuesta = input(f"Digita {i} si quieres agregar a {personaje['nombre']}:  ")

    if respuesta != "":
        numero = int(respuesta)
        if numero == i:
            grupos.append(personaje["nombre"])
            total_puntos += personaje["nivel"]
            if personaje["universo"] == "DC":
                dc.append(personaje["nombre"])
            elif personaje["universo"] == "Marvel":
                marvel.append(personaje["nombre"])
        else:
            print(f"numero incorrecto, {personaje['nombre']} es el {i}.")

print("-" * 60)
print(f"Tu grupo es {grupos}")
print(f"Tu nivel para combate es {total_puntos}")
print(f"Tu grupo tiene {len(dc)} personajes de DC y {len(marvel)} personajes de Marvel")

