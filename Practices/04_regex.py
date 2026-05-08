""" 
Validar si un texto empieza con cierta palabra
Dado un string, verifica si empieza con 
la palabra "Hola".

Ejemplo:

"Hola mundo" ✅

"Adiós mundo" ❌


"""
import re


def start():
    word = input("Escribe 'Hola mundo': ")
    print(re.match("Hola mundo", word))


start()

