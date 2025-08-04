# Loops

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
    if my_condition == 6:
        print("Se detuvo, llegó al Break ✋")
        break

print("-------------------------------------")

# C012: Bucle While (else)
my_other_condition = 0
while my_other_condition < 10:
    print(my_other_condition)
    my_other_condition += 2
else:
    print("Mi condición es mayor o igual que 10 👈")


print("-------------------------------------")

# For: Para iterar un listado de elemento
houses = ["Stark", "Arryn", "Tully", "Greyjoy", "Lannister", "Baratheon"]
for house in houses:
    print(house)


print("-------------------------------------")
# For para un dict
bands = {
    "KPOP": {"Twice", "Red Velvet", "Sunmi", "Blackpink"},
    "Trash": {"Megadeth", "Metallica", "Slayer"},
    "Rap": {"Eminem", "Snoop Dogg", "2Pac", "Ice Cube"},
}

# Los indices (keys)
for genre in bands:
    print(genre)

print("-------")
# Iteración de los valores
for band_group in bands.values():
    for band in band_group:
        if band == "Metallica":
            print("Master, Master")

print("-------")
for genre, group in bands.items():
    print(f"{genre}: {group}")

print("-------------------------------------")
# For con else
names = ["Arya", "Jon", "Bran", "Sansa"]
for name in names:
    print(f"Revisando: {name}")
    if name == "Cersei":
        print("Cersei encontrada 👀")
        break
else:
    print("Cersei no estaba en la lista")


print("-------------------------------------")
# Ejecución continua
# C013: Continue
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number == 3:
        print("Saltando el 3")
        continue
    print(f"Número: {number}")
else:
    print("El bucle terminó sin break")
