# Funcion de orden superior
# C019: Función de orden superior
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


""" 
Ejercicio 2 – Función que devuelve otra función

Crea una función llamada crear_saludador que:
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
