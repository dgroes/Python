import csv
from collections import defaultdict

# Diccionario para acumular sumas y conteos
notas = defaultdict(list)

# 1. Leer el archivo CSV
with open("./Files_to_practices/02_notas.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        asignatura = row["Asignatura"]
        nota = float(row["Nota"])
        notas[asignatura].append(nota)

# 2. Calcular promedios
promedios = {asig: sum(vals) / len(vals) for asig, vals in notas.items()}

# 3. Escribir en un nuevo archivo CSV
with open("./Files_to_practices/02_promedios.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Asignatura", "Promedio"])
    for asignatura, promedio in promedios.items():
        writer.writerow([asignatura, round(promedio, 2)])

print("Archivo 'promedios.csv' creado con éxito 🎉")
