# Retos con Python

"""
Escribe un programa que muestr por consola los números de 1 a 100 (cambos incluidos y con un salto de línea entre cada impresicón).
Sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz"
- Múltiplos de 5 por la palabra "buzz"
- Múltiplos de 3 y 3 a la vez por la palabra "fizzbuzz".
"""


def fizzbuzz():
    for index in range(1, 101):
        if (index % 5 == 0) and (index % 3 == 0):
            print("FizzBuzz")
        elif index % 3 == 0:
            print("Fizz")
        elif index % 5 == 0:
            print("Buzz")
        else:
            print(index)


fizzbuzz()


""" 
¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""
print("----------------")

def is_anagram(first, second):
    first, second = first.lower(), second.lower()

    if first == second:
        print("Ambas palabras son iguales, no es un anagrama ❌")
    elif sorted(first) == sorted(second):
        print("Es anagrama ✏️")
    else:
        print("No es anagrama ⚠️")

# Sorted ordena las lestra en una lista:: 
# sorted("roma") → ['a', 'm', 'o', 'r']
# sorted("amor") → ['a', 'm', 'o', 'r']

is_anagram("Roma", "Amor")
is_anagram("Roma", "Roma")
is_anagram("Roma", "Romaa")


"""
LA SUCESIÓN DE FIBONACCI
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
"""


"""
¿ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""


"""
INVIRTIENDO CADENAS
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""
