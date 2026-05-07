# Repaso luego de no programar por mucho tiempo, aquí se repasará a nivel global todo lo visto
# previamente en Python.

print("----Repaso----")


## 01: Variables 
''' 
En Python no hay constantes, a modo de sintaxis, es usual usar mayuscula en el nombre de la variables,
para indicar que deberá ser inmutable
'''
a = 12
print(a)

a = 13
print(type(a))

## 02: Funciones (def)

def nombreCompleto(name, last_name):
    if isinstance(name, int) or isinstance(last_name, int):
        print("No introducir números")
    else:
        print(name + ' ' + last_name)

def nombreCompletoV2(name, last_name):
    if isinstance(name, int):
        print(str(name) + ' ' + last_name)
    else:
        print('nada')


nombreCompleto('Diego', a)

nombreCompletoV2(a, 'Pastén')

## 03: Arrays (Tuplas, Listas, Dics)
print("--------Arrays-------")
print("--[Listas]--")
# Listas [mutables)]
numeros = [1, 2, 3, 4, 'cinco', 6, 'siete']

""" print(type(mi_lista))
print(mi_lista[3]) """

for numero in numeros:
    print(numero) 

for i, numero in enumerate(numeros):
    if isinstance(numero, str):
        print("Hay números en string: " + numero)
    

if 'sss' in numeros:
    print("Valor encontrado")
else:
    print("Valor no encontrado")

## def lista_buscar_string(lista):
    

# Tuplas(inmutables)
print("--(Tuplas)--")
idols_diego = 'Somi', 'Nayeon', 'Dahyun', 'Ningnig', 'Rose'
idols_kathia = 'Dahyun', 'Hwasa', 'Karina', 'Umji'

print(type(idols_diego))
print(len(idols_diego))


def idols_comparacion(primero, segundo):
    if len(primero) > len(segundo):
        print("La primera persona tiene más idols 🩷")
    else:
        print("La segunda persona tiene más idols 💖")


# pasar datos de una tupla a una lista
lista_idols = list(idols_diego)
lista_idols[0] = 'Sana'
lista_idols.insert(3, 'Solar')
print(lista_idols)

print(type(lista_idols))



idols_comparacion(idols_diego, idols_kathia)

# Diccionario {clave-valor}
print("--------diccionarios-------")
libro = {
    "nombre": "El mago",
    "autor": "John Fowles",
    "publicacion": 1965
}

print(libro)
print(libro['nombre'])
libro['autor'] = 'Bret Easton Ellis'

print(libro['autor'])

for llaves in libro:
    print(llaves)

for valores in libro:
    print(libro[valores])

for llaves, valores in libro.items():
    print(llaves, valores)


## MODIFICACIÓN DE FICHEROS



## CONEXIÓN A UNA DB