# Modulos
# Utilizar la función: "print_name" del fichero "10_functions.py"
# import 10_functions #<-- esto no funcionará

# Para acceder a un modulo, dicho modulo deberá estar
# en snake_case y no deberá empezar con un número

# Se crea un fichero "my_module.py"
import my_module  # Importación general

my_module.print_name("Peter", "Parker")


# Importación de una function
from my_module import mayoria_edad

mayoria_edad(18)


#IMportar una variable
from my_module import variable
print(variable)


# Importación de Modulos del sistema (propios de Python) 🌎
import math
print(math.pi)

# Potencia, 2 elevado a 8
print(math.pow(2, 8))

# Importar solo una función propia de .math y con un alías:
from math import pi as PI_VALUE
print(PI_VALUE)