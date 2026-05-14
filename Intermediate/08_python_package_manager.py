### Python Package Manager ###
## Es una herramienta que permite instalar, actualizar y gestionar paquetes de Python.

## PIP: Es el gestor de paquetes oficial de Python.
# Permite instalar paquetes desde el Python Package Index (PyPI) y otros repositorios.

# import pandas <-- Esto no funciona sin antes instalarlo con pip install numpy
# import numpy <-- Esto no funciona

# Lo que se deberá hacer, será instalar PIP
## Para saber si está instalado, será con "pip --version"

import numpy # pip install numpy
import pandas # pip install pandas
import requests # pip install requests

print("***NUMPY***")
print(f"- numpy versión: {numpy.version.version}")

array = numpy.array([1, 3, 5, 7, 9])

print(type(array))

print(array * 2)


response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
# Listar los paquetes instalados 

print(response.status_code)
print(response.json())


## Package arithmetics
print("\n Importar paquetes propios")
from my_package import arithmetics


print(arithmetics.sum(1, 6))