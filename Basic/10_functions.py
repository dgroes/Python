# Funciones
def my_function():
    print("Hola")


my_function()

print("-----------")


# Función + if
def mayoria_edad(edad):
    if edad >= 18:
        print("Eres mayor de edad ")
    else:
        print("Eres menor de edad, algo ahí")


mayoria_edad(18)


# Con return
def sum_two_values(num_one, num_two):
    print(num_one + num_two)


sum_two_values(5, 3)


# Devuelve el resultado, pero se deberá imprimir de igual manera
def sum_two_valuess(num_one, num_two):
    result = num_one + num_two
    return result
    # o tambien: return num_one + num_two


my_result = sum_two_valuess(5, 2)
print(my_result)
# o tambien: print(sum_two_valuess(1, 3))

print("-----------")
# Asignacion de orden propio


def print_name(name, surname):
    print(f"Tu nombre es: {name} {surname}")


# aquí se le puede asignar por orden personalizado
print_name(surname="O'hara", name="Miguel")


# Definir un valor por defecto en el parametro
def print_name_default(name, surname, alias="sin alias"):
    print(f"{name} {surname} {alias}")


print_name_default("Miguel", "O'Hara", "Spider-Man")
print_name_default("Miguel", "O'Hara")

# Argumengos posicionales:
# C014: Argumentos arbitrarios (args)
def print_texts(*text):
    for text in text:
        print(text)
 
print_texts("Python", "PHP", "Javascript")
