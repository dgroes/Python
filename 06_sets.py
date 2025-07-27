# Set {}
my_set = set()
print(type(my_set))

# Diccionario vacio
my_set_0 = {}
print(type(my_set_0))  # <- tipo "dic"

# Set con valores
my_other_set = {"Python", "PHP", "JavaScript"}
print(type(my_other_set))
print(my_other_set)

# Cuantos elementos hay: len()
print(len(my_other_set))

# Acceder a un elemento , esto no funciona
# print(my_other_set[1])
""" 
Un set no es una estrucura ordenada, 
su indice ya no importa. 
Su orden de elemento no es ordenada.
[En cada print se puede ver que siempre 
se obtiene un orden distinto]
"""

# Add añade el nuevo elemento. sin orden
my_other_set.add("C#")
print(my_other_set)

## Add repetido. No se puede repetir un elemento en su contenido
my_other_set.add("C#")
print(my_other_set)
print("------------------------------")

# Comprobación de si existe un elemento
print("Java" in my_other_set)  # False
print("C#" in my_other_set)  # True
print("------------------------------")

# Quitar un elemento
my_other_set.remove("JavaScript")
print(my_other_set)

# Vaciar el set
my_other_set.clear()
print(my_other_set)
print(len(my_other_set))

# Eliminar el set
del my_other_set
# print(my_other_set) <-[error] ya no existe el set
print("------------------------------")

# Transformar un set a list (no es muy útil)
""" 
Un set tiene elementos desordenados. Si ahora es una
lista se puede acceder a sus index, pero si no hay 
un orden inicial sería poco útil hacerlo
"""
my_set = {"Verde", "Rojo", "Morado"}
my_list = list(my_set)
print(my_list)

# Unir 2 sets
my_other_set = {"Red Dragon", "Filterworld", "Digital minimalism"}
my_new_set = my_set.union(my_other_set)
print(my_new_set)

# Diferencia. 
# Imprime los que son parte de my_new_set y que no están dentro del set my_set
print(my_new_set.difference(my_set))