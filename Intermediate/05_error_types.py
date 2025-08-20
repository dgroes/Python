# Error Types
print("----------(ErrorTypes)----------")

print("----------[SyntaxError]----------")
## SyntaxError
# print "The winter is coming"
""" 
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
"""
print("The winter is coming")

print("----------[NameError]----------")
## NameError
""" 
NameError: name 'house' is not defined
"""
house = "Stark"
print(house)

print("----------[IndexError]----------")
## IndexError
my_list = [
    "Hierro",
    "Latón",
    "Bronce",
    "Acero",
    "Estaño",
    "Oro Rojo",
    "Plata",
    "Oro Amarillo",
    "Plomo",
    "Peltre",
    "Platino",
    "Oro Blannco",
    "Acero Valyrio",
]

""" 
IndexError: list index out of range
"""
print(my_list[33])