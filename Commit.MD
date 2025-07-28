# C01: snake_case
La convención general es escribirlo en "**snake_case**": `MyVariable` = `my_variable`.
# C02: Anotacion de Tipo
Es una caracteristica añadida en **Pyton 3.5**. El cual permite anotar las **variables, funciones, argumentos y retornos con tipos**, como una forma de documentación y verificación opcional.
```py
def saludar(nombre: str) -> str:
    return "Hola " + nombre
```
- `nombre: str` → tipo del argumento
- `-> str` → tipo del valor de retorno
- Pero **no se aplican en tiempo de ejecución** (Python no lanza error si le pasas un número, por ejemplo).

Pues como no se aplican en tiempo de ejcucuión usualmente se utilizan con **herramientas de chequeo estático de tipos**, como:
- mypy 
- pyright (el motor detrás del soporte de Python en VSCode)
- pylance (extensión de análisis para VSCode)
## Esto hace que Python sea un lenguaje "tipado estático"? 
No. Python siguie **siendo un lenguaje de tipado dinámico**, pero **ahora soporta anotaciones estáticas**.
# C03: División entera (//)
En Python existe la división entera o división de piso (floor division). Este operador toma dos números y realiza la división, pero en lugar de devolver un resultado con decimales, **redondea hacia abajo al entero más cercano**. En otras palabras descarta la parte fraccionaria del resultado:
```py
# Ejemplo:
resultado_division_normal = 10 / 3  # Resultado: 3.333...
resultado_division_entera = 10 // 3 # Resultado: 3
```
La división normal con una barra (`/`) devuelve un número flotante con decimales, mientras que la división entera con doble barra (`//`) devuelve un úmero entero, resultado de redondear hacia abajo el resultado de la división normal.
> El operador `//` es equivalente a usar la función `math.floor()` en Python.
# C04: Comparaciones entre String (ASCII)
En Python **las comparaciones entre strings se hacen siguiendo el orden alfabético lexicográfico, basado en los valores Unicode (ASCII)** de cada carácter de **izquiera a derecha**.
Cada carácter tiene un valor numérico. por ejemplo:
| Letra | Código ASCII |
| ----- | ------------ |
| H     | 72           |
| P     | 80           |
| o     | 111          |
| y     | 121          |
| t     | 116          |
Siguiendo lo anterior, cuando en python se evalua lo siguiente:
```python
print("Hola" > "Python")  # False
```
Está comparando letra por letra:
`'H'` (72) vs `'P'` (80) → como 72 < 80, entonces `"Hola"` < `"Python"` → Resultado: False para `Hola > Python`.
# C05: Operadores lógicos
| Operador | Significado     | Devuelve `True` si...                       |
| -------- | --------------- | ------------------------------------------- |
| `and`    | Y lógico        | Ambas condiciones son `True`                |
| `or`     | O lógico        | Al menos una condición es `True`            |
| `not`    | Negación lógica | Invierte el valor lógico (`True` ⇄ `False`) |.

| A     | B     | A and B |
| ----- | ----- | ------- |
| False | False | False   |
| False | True  | False   |
| True  | False | False   |
| True  | True  | True    |

| A     | B     | A or B |
| ----- | ----- | ------ |
| False | False | False  |
| False | True  | True   |
| True  | False | True   |
| True  | True  | True   |

| A     | not A |
| ----- | ----- |
| False | True  |
| True  | False |
# C06: Lista
Una **lista** es una estrucura de datos **integrada** (built-in) que **puede almacenar elementos de difentes tipos**:
```py
mi_lista = [1, "Hola", True, 3.14]
```
- **Es dinámica**: puede crecer o reducirse.
- Se puede mezclar tipos de datos.
- Se accede por índices (como en un array).

**Python no tiene arrays como tal** integrados en el lenguaje base como otros lenguajes. Pero si se puede usar arrays si se importa el módulo `array`:
```py
import array
mi_array = array.array('i', [1, 2, 3, 4])
```
- Solo permite **datos del mismo tipo** ('i' es tipo entero).
Es más **eficiente** en memoria que una lista para  grandes cantidades de datos del mismo tipo.
Diferencias Clave:

| Característica          | Lista (`list`)         | Array (`array.array`)                    |
| ----------------------- | ---------------------- | ---------------------------------------- |
| Tipos de datos          | Mezclados              | Solo un tipo de dato                     |
| Parte del núcleo Python | Sí                     | No, requiere `import array`              |
| Flexible                | Muy flexible           | Más estricto                             |
| Usos comunes            | Genérico, uso diario   | Eficiencia y uso técnico específico      |
| Ejemplo de creación     | `mi_lista = [1, 2, 3]` | `mi_array = array.array('i', [1, 2, 3])` |
# C07: Constantes
En Python **no existen las variables constantes**, pero **hay una convención para representar constantes**. En Python, se usan **letras mayúsculas** para indicar que una variable debe ser trata como constante. por ejemplo:
```py
PI = 3.14159
MAX_USERS = 100
URL_BASE = "https://api.ejemplo.com"
```
💎 Estas variables **si se pueden modificar**, pero **por convención no se debería hacerlo**
**Forzado de constantes**
Se puede usar una herramienta más avanzada para forzar constantes como:
- clases personalizadas
- módulos externos como `typing.Final` (desde Python 3.8).
Ejemplo con `Final`:
```py
from typing import Final

PI: Final = 3.14159
PI = 3  # Esto lanzaría una advertencia en linters, pero Python lo permite igual en tiempo de ejecución.
```  
# C08: Tuplas
Una **tupla** en Python es una colección **ordenada** e **inmutable** de elementos. Similar a una **lista**, pero con diferencia:
| Característica      | Lista (`list`)                | Tupla (`tuple`)                              |
| ------------------- | ----------------------------- | -------------------------------------------- |
| Sintaxis            | `[1, 2, 3]`                   | `(1, 2, 3)`                                  |
| Mutabilidad         | ✅ **Mutable** (puede cambiar) | ❌ **Inmutable** (no puede cambiar)           |
| Rendimiento         | Más lenta                     | Más rápida                                   |
| Uso típico          | Datos que cambian             | Datos fijos (como coordenadas, fechas, etc.) |
| Métodos disponibles | Muchos (como `.append()`)     | Muy pocos (`.count()`, `.index()`)           |

Un ejemplo en código sería
```py
# Lista
lista = [1, 2, 3]
lista.append(4)  # ✅ Se puede modificar

# Tupla
tupla = (1, 2, 3)
# tupla.append(4)  ❌ Error: las tuplas no se pueden modificar
```
Una tupla entonces debería ser una opción cuando:
- Cuando **no se quiere que los datos se modifiquen**.
- Cuando se necesita **más eficiencia** (las tuplas consumen menos memoria).
- Cuando los datos son **semánticamente constantes** (como (latitud, longitud)).
# C09: Sets
En Python, un `set` (conjunto) es una **colección desordenada, sin elementos duplicados y mutable** (se puede cambiar después de ser creada)
| Característica                    | Detalles                                                                   |
| --------------------------------- | -------------------------------------------------------------------------- |
| ✅ Elementos únicos                | No permite duplicados. `{1, 2, 2, 3}` → `{1, 2, 3}`                        |
| ❌ No ordenado                     | No garantiza orden al imprimirlo o recorrerlo                              |
| ✅ Mutable                         | Puedes agregar o eliminar elementos con métodos como `.add()`, `.remove()` |
| ❌ No indexable                    | No puedes acceder con índices como `mi_set[0]`                             |
| ✅ Permite operaciones de conjunto | unión, intersección, diferencia, etc.                                      |
Un ejemplo en código seria:
```py
my_set = {1, 2, 3, 4}
print(my_set)  # {1, 2, 3, 4}

my_set.add(5)
print(my_set)  # {1, 2, 3, 4, 5}

my_set.add(3)
print(my_set)  # {1, 2, 3, 4, 5} → 3 ya existía, no se repite
```
Algunas operaciones entres sets:
```py
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # Unión → {1, 2, 3, 4, 5}
print(a & b)  # Intersección → {3}
print(a - b)  # Diferencia → {1, 2}
print(a ^ b)  # Diferencia simétrica → {1, 2, 4, 5}
```
s
# C010: Diccionario
Un diccionario es una **colección de datos no ordenada y mutable** que **almacena pares clave-valor**.
```py
persona = {
    "nombre": "Diego",
    "edad": 30,
    "pais": "Chile"
}
```
- `"nombre"`, `"edad"`, `"pais"` son las claves (keys).
- `"Diego"`, `30`, `"Chile"` son los valores (values).
Entonces se pude acceder de esta forma:
```py
print(persona["nombre"])  # -> Diego
```
Una diferencia clave con otros conjunto de elementos son sus indices. Solo se puden **acceder a los indices a travez de su clave**. por ejemplo:
```py
frutas = {
    "roja": "manzana",
    "amarilla": "banana",
    "verde": "pera"
}
print(frutas["amarilla"])  # "banana"
```
pero si trato de acceder a manzaja de esta forma daría un error:
```py
print(frutas[0])  # "banana"
```
Para **acceder a dicho elemento solo sirve su clave**
## Diferencia con un set
Un set es una **colección no ordenada**, **sin elementos duplicados**. Se usa, por ejemplo para eliminar duplicados:
```py
mi_set = {1, 2, 3, 3, 4}
print(mi_set)  # -> {1, 2, 3, 4}
```
Tanto `set` como `dict` utilizan llaves (`{}`) como delimitadores, pero son estruccuras distintas:
| Característica | Diccionario (`dict`)     | Conjunto (`set`)            |
| -------------- | ------------------------ | --------------------------- |
| Sintaxis       | `{clave: valor}`         | `{elemento, elemento}`      |
| Tipo de datos  | Pares clave-valor        | Valores únicos              |
| Acceso         | Por clave (`dic['key']`) | No admite acceso por índice |
| Ejemplo        | `{"nombre": "Diego"}`    | `{1, 2, 3}`                 |
s
# C011: dict.fromkeys()
El método `dic.fromkeys()` lo que hace es crear un nuevo diccionario usando: 
- **Una secuencia de claves**
- Un **valor común para todas esas claves**
```py
claves = ["Matemáticas", "Física", "Lenguaje"]
notas = dict.fromkeys(claves, 0)

print(notas)
# {'Matemáticas': 0, 'Física': 0, 'Lenguaje': 0}
```
s
# C012:
# C013:
# C014:
# C015:
# C016:
# C017:
# C018:
# C019:
# C020:
# C021:
# C022:
# C023:
# C024:
# C025:
# C026:
# C027:
# C028:
# C029:
# C030: