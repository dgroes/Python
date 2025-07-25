# Ejemplo de creación de variables
# Escribr las variables en 'snake_case'
name = "Diego"
age = 27
pi = 3.14159
is_chilean = True # C01: snake_case
name = "Andrés" #Cambio de "valor" de la variable
print(type(is_chilean))
print(name, age, is_chilean) # Concatenación de variables
print('-----------------------------')

# Transformar float a string:
float_variable = 12.4
float_to_str = str(float_variable)
print(float_to_str, type(float_to_str))
print('-----------------------------')

# Transformar string a int
str_variable = "870621345"
str_to_int = int(str_variable)
print(str_to_int, type(str_to_int))
print('-----------------------------')

#NoneType
print(type(print('Cadea de texto')))
print('-----------------------------')

# Variables de una sola línea
brand, model, frets, color = "Squier", "Afinity", 21, "Butterscotch Blonde"
print("Guitar", brand, model, "frets numbers:", frets, "and color:",color)
print('-----------------------------')

# _FUNCIONES DEL SISTEMA_: Largo de una variable
print("Andrés tiene:", len(name), "letras.") #Andrés
print('-----------------------------')

# Input + variable
edad = input("Que edad tienes? ")
print('El usuario tiene', edad, 'años')
print('-----------------------------')

# C02: Anotacion de Tipo
# Forzado de tipado?
address: str = "Neverland"
address = 22
print(address)

