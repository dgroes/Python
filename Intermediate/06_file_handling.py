# File Handling (Manejo de ficheros)
# Intermediate\my_file.txt

"""encoding="utf-8" <- Para tildes"""

print("[.txt]")
## .txt file
txt_file = open("./my_file.txt", "r+", encoding="utf-8")
# Leer fichero
# print(txt_file.read())

# Leer los primeros 10 caracteres
# print(txt_file.read(10))

# Lecutra línea a línea
# print(txt_file.readline())

# Lectura de lineas
## generando un list de string de cada string converttida en un elemento de la list
# print(txt_file.readlines())
for line in txt_file.readlines():
    print(f"- {line}")

# Escribir, con un salto de línea
txt_file.write("\nVientos de Invierno")
txt_file.close()


# Crear fichero
txt_new_file = open("./my_new_file.txt", "w+", encoding="utf-8")
txt_new_file.write(
    "Soy el vigilante del Muro. Soy el fuego que arde contra el frío, la luz que trae el amanecer, el cuerno que despierta a los durmientes, el escudo que defiende los reinos de los hombres.\nEntrego mi vida y mi honor a la Guardia de la Noche, durante esta noche y todas las que estén por venir"
)
# Cerrar el fichero
txt_new_file.close()

# Borrar el fichero
# import os
# os.remove("./my_new_file.txt")


## .json file

print("-----[json]-----")
import json

# Creación del fichero json si no existe
json_file = open("./my_json_file.json", "w+")

json_test = {
    "locations": [
        {
            "name": "Desembarco del Rey",
            "region": "Corona",
            "description": "Capital de los Siete Reinos y sede del Trono de Hierro.",
        },
        {
            "name": "El Muro",
            "region": "El Norte",
            "description": "Gigantesca muralla de hielo que separa los Siete Reinos de las tierras salvajes.",
        },
    ],
}

# Añadir el diccionario creado al fichero creado
json.dump(json_test, json_file, indent=2)

json_file.close()

with open("./my_json_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("./my_json_file.json"))
print(json_dict)
print("->", json_dict["locations"][0]["region"])

# C22: with + file
# .csv file
import csv

# Abrir archivo en modo escritura
with open("./my_csv_file.csv", "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)

    # Escribir cabecera
    writer.writerow(["Título", "Autor", "Año de publicación"])

    # Escribir filas
    writer.writerow(["Juego de Tronos", "George R. R. Martin", 1996])
    writer.writerow(["Choque de Reyes", "George R. R. Martin", 1998])
    writer.writerow(["Tormenta de Espadas", "George R. R. Martin", 2000])
    writer.writerow(["Festín de Cuervos", "George R. R. Martin", 2005])
    writer.writerow(["Danza de Dragones", "George R. R. Martin", 2011])
