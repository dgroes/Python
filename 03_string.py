my_strin = "Mi string"
my_other_string = "Mi otro string"
print(len(my_strin))
print(len(my_other_string))
print(my_strin + " " + my_other_string)

my_line_string = "Este es un    String\ncon salgo de líena"
print(my_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\\Este es un String \nescapado"
print(my_scape_string)

print("----------------------")
name, surname, age = "Jon", "Snow", 24
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %s" % (name, surname, age))

print(f"Mi nombre es {name} {surname} y mi edad es {age}")
print("----------------------")

# Desempaquetado de caracteres
language = "Python"
a, b, c, d, e, f = language
print(a)
print(b)
print("----------------------")

# División
language_slice = language[1:3]
print(language_slice)
language_slice = language[2:]
print(language_slice)
language_slice = language[-3]
print(language_slice)
language_slice = language[0:6:2]
print(language_slice)
print("----------------------")

# Reverse
reversed_languaje = language[::-1]
print(reversed_languaje)

# Funciones del sistema
print(len("Arya"))
print(language.capitalize())  # Primera en mayus
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.startswith("Py"))
