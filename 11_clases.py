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
        self.full_name = f"{name} {surname}"

    # aquí deberi pasarle "self" para acceder a usus propiedades
    def walk(self):
        print(f"{self.full_name} está caminando")


person = MyPerson("Christopher", "Smith")
print(person.full_name)
person.walk()
