# Condicionales
# Flujos de ejecución del código

my_condition = False

if my_condition:
    print("Es True")
else: 
    print("Es False")



jon_snow = {"Nombre": "Jon", "Apellido": "Snow"}

apellidos_bastardos = ["Snow", "Sand", "Stone", "Flowers", "Hill", "Storm", "Pyke", "Waters"]

apellido = jon_snow["Apellido"]

if apellido in apellidos_bastardos:
    print("Es bastardo")
else:
    print("No es bastardo")

print("-----------------------------------------")
personajes = [
    {"Nombre": "Jon", "Apellido": "Snow"},
    {"Nombre": "Oberyn", "Apellido": "Martell"},
    {"Nombre": "Ellaria", "Apellido": "Sand"},
    {"Nombre": "Gendry", "Apellido": "Waters"},
]

apellidos_bastardos = ["Snow", "Sand", "Stone", "Flowers", "Hill", "Storm", "Pyke", "Waters"]

for p in personajes:
    if p["Apellido"] in apellidos_bastardos:
        print(f"{p['Nombre']} {p['Apellido']} es bastardo")
    else:
        print(f"{p['Nombre']} {p['Apellido']} no es bastardo")