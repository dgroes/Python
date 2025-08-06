# Operadores
print("OPERADORES➗")
print(5 / 4)
12 + 14  # Esto no saldría, faltaría el print
print(10 % 3)
print(10 // 3)  # C03: División entera (//)
print(2**3)  # Exponente 2 * 2 * 2
print("--------------------------")

print("Bucket" + "head")  # Se puede concatenar con '+'
# print("Bucket" - "head") <-- Esto daría un error
# print("John " + 5) Esto daría error, esto no es JS 😄
print("John " + str(5))
print("number 9 " * 7)  # Multiplicar una palabra
print("--------------------------")

# Operadores comparativos
print(5 > 10)  # 5 no es mayor que 10, da False
print(8 == 8)  # 8 es igual a 8, da True
print(4 <= 10)  # 4 es menor o igual a 10. da True
print(14 != 14)  # 14 no es distinto de 14, da False
print("Diego" == "Diego")  # Esto da True
print(5 == "5")  # Esto da False
print(3 > 4 == 2)  # False
print(3 < 4 < 5)  # 3 es menor que 4, 4 menor que 5
print("-------------------------")

# C04: Comparaciones entre String (ASCII)
print("Hola" > "Python")  # False, porque 'H' < 'P'
print("Python" == "Python")  # True, son exactamente iguales
print("Hola" < "Python")  # True, porque 'H' < 'P'
print("Hola" >= "Python")  # False, 'H' < 'P'
print("Hola" <= "Python")  # True, 'H' < 'P'
print("Hola" == "Python")  # False, no son iguales
print("Hola" != "Python")  # True, son diferentes
print("--------------------------")
print(" ")

# C05: Operadores lógicos
# Operadores Lógicos
# --- AND ---
# Solo devuelve True si ambas condiciones son True
print("Operador AND")
print(3 > 4 and 2 > 3)   # False and False => False
print(3 < 4 and 2 > 1)   # True and True   => True
print(3 < 4 and 2 > 5)   # True and False  => False

# --- OR ---
# Devuelve True si al menos una de las condiciones es True
print("Operador OR")
print(3 > 4 or 2 > 3)    # False or False  => False
print(3 < 4 or 2 > 3)    # True or False   => True
print(3 > 4 or 2 < 3)    # False or True   => True

# --- NOT ---
# Invierte el valor lógico (True → False, False → True)
print("Operador NOT")
print(not (3 > 4))       # not False       => True
print(not (3 < 4))       # not True        => False

# --- Combinando varios ---
print("Combinando comparadores")
print((3 < 4 and 5 > 2) or not (4 == 4))  
# (True and True) or not True
# True or False => True

print((3 > 4 or 5 < 2) and not (2 != 2))
# (False or False) and not False
# False and True => False