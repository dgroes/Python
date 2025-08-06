# Diccionarios
# C010: Diccionario

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Jon", "Apellido": "Snow", "Edad": 21}
print(my_other_dict)
# print(my_other_dict[0])

print("---------------------------------------------")
my_dict = {
    "Nombre": "Daenerys Targaryen",
    "Casa": "Targaryen",
    "Titulos": {
        "Princesa de Rocadragón",
        "Khaleesi de los Dothraki",
        "Reina de Meereen",
    },
    "edad": 16,
}

print(my_dict)
print("Longitud:", len(my_dict))  # Cantidad de claves
print("-----------------------------------------")

# Mostra valor
print(my_dict["Nombre"])  # Mostrar el valor de dicha clave "Nombre"

# Actualizar un valor de una clave
my_dict["Nombre"] = "Daenerys de la Casa Targaryen"
print(my_dict["Nombre"])

# Añadir una nueva claver + valor (elemento)
my_dict["Estado"] = True
print(my_dict)

# Eliminar un elemento
del my_dict["Estado"]
print(my_dict)

print("-----------------------------------------")
# Saber si existe una clave en el dict
print("Casa" in my_dict)  # True

#
print("-", my_dict.items())
print("-", my_dict.keys())  # Mostrar listado de keys
print("-", my_dict.values())  # Mostrar listado de values

print("--------------------------------------------")
# C011: dict.fromkeys()
lenguajes = ["Python", "PHP", "C#"]
backend = dict.fromkeys(lenguajes, "Backend")
print(backend)


# Crear un nuevo diccionario utilizando las claves de otro
new_dict = dict.fromkeys(my_dict)
print(new_dict) # <-- {'Nombre': None, 'Casa': None, 'Titulos': None, 'edad': None}
# Poblar nuevo dict


keys = ["Nombre", "Casa", "Titulos", "edad"]
values = ["Eddard Stark", "Stark", "Señor de Invernalia", 36]

new_dict = dict(zip(keys, values))
print("-",new_dict)