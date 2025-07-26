# Lista
# C06: Lista
# Inicializando una lista vacía
my_list = list()
my_other_list = []
print(type(my_list))
print(len(my_list))  # 0, aun no tiene elementos dentro
print(type([1, 2, 3]))
print(type(list((1, 2, 3))))

my_list = [1, "Davos", 3.14, 4, 555, "💀", "💀", 13.2, False]
print(my_list)
print(len(my_list))  # 9, ahora tiene 9 elementos dentro
print("--------------------------------------------")

## Accediendo a los datos
# print(my_list[-11]) <-- Da error
print(my_list[2])
print(type(my_list[6]))
print(my_list[-3])
print(my_list.count("💀"))  # 2, ya que se repite ese emoji dos veces

print("--------------------------------------------")
new_list = [
    "Daenerys",
    "Targaryen",
    16,
]
name, surname, age = (
    new_list  # Se ledeven pasar todos los elementos, ni uno más ni uno menos, en este caso sería 3 elementos
)
print(surname)  # imprime: Targaryen

new_guitar = [21, "Afinity", 1965, "Fender", "butterscotch blonde"]
brand, model, year, color, freets = (
    new_guitar[3],
    new_guitar[1],
    new_guitar[2],
    new_guitar[4],
    new_guitar[0],
)
print(color)

print(new_list + new_guitar)
print("--------------------------------------------")

new_guitar = "Python"
print(new_guitar)

book_list = [
    "Red Dragon",
    "A Feast for Crows",
    "The Time Machine",
    "The Godfather",
    "The Godfather",
]
print(book_list)
book_list.append("1984")  # Append inserta al final
book_list.insert(1, "Can't Hurt Me")  # Insertar en una pocición especifica
book_list.remove("The Time Machine")  # Remover un elemento
book_list.remove(
    "The Godfather"
)  # 'The Godfather' esta repedio, eliminaría el primer elemeto que coincida

print(book_list)
print(book_list.pop())  # Eliminar el último elemento de la lista
my_pop_element = book_list.pop(3)  # Eliminar por indice. Pop() es util para quitar un elemento y guardarlo para su uso más tarde
print("El elemento eliminado fue: " + my_pop_element)
print("--------------------------------------------")

print(book_list)
old = book_list[2]
new = book_list[2] = "Shutter Island" # Cambiar un elemento por otro nuevo, especificando el index y el nuevo dato
print("Se cambia el elemento:" + old + " por el nuevo elemento: " + new)
print("--------------------------------------------")

print(book_list)
new_list_book = book_list.copy()
print("Copia de la lista:", new_list_book)
print("--------------------------------------------")

del book_list[0] # Del elimina por completo un elemento por el 'indice'
print(book_list)

book_list.clear() # Vaciar la lista completa
print(book_list)
print("--------------------------------------------")

new_list_book.reverse() # Invertir el orden de la lista
print(new_list_book)

new_list_book.sort() # El sort() vacio ordena por alfabetico en Str 
print(new_list_book)

print(new_list_book[2:3])
