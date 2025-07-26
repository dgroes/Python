# Tuplas: Son "inmutables"
# C08: Tuplas

my_tuple = tuple()
my_other_tuple = ("Jaime", "Lannister")
print(type(my_tuple))  # <- <class 'tuple'>

my_tuple = ("Ned", "Stark", 35, False, "Stark")
print(my_tuple)
print("--------------------------------------------")

# Accediendo a elementos
print(my_tuple[1])
print(my_tuple[3])
# print(my_tuple[12])  <- [Error] no hay dicha cantidad de elementos

print(my_tuple.count("Stark"))  # Conteo de un elemento
print(my_tuple.index(False))  # Devuelve el index de un element
print("--------------------------------------------")

# my_tuple.append("Hola") <- tuple tiene pocas funciones, append no es una de elllas
""" my_tuple[3] = True
print(my_tuple) <- Tampoco se le pueden añadir más elementos"""

# Sumando 2 tuplas
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)
print(type(my_sum_tuple))
print(my_sum_tuple[2:4])
print("--------------------------------------------")

# No se puede sumar una tupla con una lista:
# my_list = [1, 2, 3]
# my_tupla = (4, 5, 6)
# my_sum_list_tuple = my_list + my_tupla
# print(my_sum_list_tuple)

# Transformar tupla a una lista
my_tuple = list(my_tuple)
print(type(my_tuple))
my_tuple.append("Melisandre") # Ahora dichos elementos son parte de una lista, ahora se pude modificar
print(my_tuple)

# Ahora incluso se puede nuevamente convertir en tupla, volviendo a ser inmutable
my_tuple = tuple(my_tuple)
print(type(my_tuple))
print("--------------------------------------------")

#Es inmutable pero "si" se puede borrar su contenido
del my_tuple
# print(my_tuple) # Eliminada, ya no exite la tupla