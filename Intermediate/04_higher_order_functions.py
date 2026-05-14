# Funcion de orden superior
# C19: Función de orden superior
from functools import reduce

"""
Ejercicio 1 – Función que recibe otra función.

Crea una función llamada procesar_lista que: Reciba una lista de números y una función como parámetros.
Devuelva una nueva lista con el resultado de aplicar esa función a cada número.
No uses map en este ejercicio, hazlo con un bucle.
"""

print("----------01----------")

lista_numeros = [1, 2, 5, 8, 3, 0, 33]


def sumar_uno(numbero):
    return numbero + 1


def procesar_lista(lista, funcion):
    nueva_lista = []
    for elemento in lista:
        nueva_lista.append(funcion(elemento))
    return nueva_lista


print(procesar_lista(lista_numeros, sumar_uno))


# Closure
# C20: Función Cerrada (closure)
""" 
Función que devuelve otra función
Una función llamada crear_saludador que:
Reciba un nombre como parámetro.
Devuelva una nueva función que, cuando se ejecute, imprima "Hola, <nombre>".
"""
print("----------02----------")


def crear_saludador(nombre):
    def saludar():
        print(f"Hola, {nombre}")

    return saludar


saludo_a_aemon = crear_saludador("Aemon Targaryen")
saludo_a_aemon()  # Hola, Aemon Targaryen

print("----------03----------")
# Built-in Higher order functions
# C21: Built-in Higher Order Functions

# Map
def multiply_two(number):
    return number * 2


numbers = [2, 3, 5, 8]

print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers))) # <- con lambda

# Filter
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(is_even, numbers)
print(list(even_numbers))

print(f"\n ***Reduce***")

# C26: Reduce
# Reduce 
def sum_two_values(first, second):
    return first + second

print(reduce(sum_two_values, numbers))