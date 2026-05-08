# Expresión regular: C23: Regular expressions
print("---[Regular Expression (Regex)]---")

import re

texto = "Mi número es 987654321 y el código es ABC123"

# Buscar al inicio (no encuentra porque no empieza con números)
print(re.match(r"\d+", texto))  # <- None

# Buscar en cualquier parte
print(re.search(r"\d+", texto).group())  # → "987654321"

# Buscar todas las coincidencias
print(re.findall(r"[A-Z]{3}\d{3}", texto))  # → ["ABC123"]

# Reemplazar
print(re.sub(r"\d", "*", texto))  
# → "Mi número es ********* y el código es ABC***"

