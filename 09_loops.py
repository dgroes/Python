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
houses = ["Stark", "Arryn", 'Tully', 'Greyjoy', 'Lannister', 'Baratheon']
for house in houses:
    print(house)