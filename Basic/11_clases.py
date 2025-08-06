# Clases
# Las clases en CamelCase
class EmptyPerson:
    pass


print(EmptyPerson)


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

        # Propiedad que solo se "define" dentro de la clase
        self.defecto = "propiedad por defecto"


my_person = Person("Bruce", "Banner")
print(my_person.defecto)


# Otro ejemplo
class MyPerson:
    def __init__(self, name, surname):
        self.full_name = f"{name} {surname} 🧔"

    # aquí deberi pasarle "self" para acceder a usus propiedades
    def walk(self):
        print(f"{self.full_name} está caminando")


person = MyPerson("Christopher", "Smith")
print(person.full_name)
person.walk()

print("--------------------------------------")

# Datos privados
class Cat:
    def __init__(self, name, age, color, owner):
        self.cat_date = f"{name}, tiene {age} años y es de color {color} 🐈"
        self.__owner = owner # Propiedad privada

    def get_name(self):
        return self.__owner # Método público para acceder al atributo privado

my_cat = Cat("Dalpo", 3, "Gris con manchas blancas", "Diego")
print(my_cat.cat_date)
print(my_cat.get_name())

# print(my_cat.__owner) <-- Error: AttributeError
# En este caso pasamos el atributo privado a un método 
# public para poder acceder a el

        