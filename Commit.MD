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
# C10: Diccionario
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
# C11: dict.fromkeys()
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
# C12: Bucle While (else)
El bucle `while` es similar que en muchos lenguajes, en Python tiene una particularidad, usando un `else`. El cual dicha condición será **cuando se recorra todo el bucle sin haber caido en un `break` previo**. Por ejemplo:
```py
n = 0

while n < 5:
    print(n)
    n += 1
else:
    print("El while terminó normalmente")
#Su salida:
""" 
0
1
2
3
4
El while terminó normalmente
"""
```
s
# C13: Continue
`continue` lo que hace es **saltar el resto del código en la iteración actual** y pasa directamente a la siguiente vuelta del `for` o `while`.
```py
for name in ["Arya", "Jon", "Sansa"]:
    if name == "Jon":
        continue  # Salta este y pasa al siguiente
    print(name)

# Resultado:
Arya
Sansa
```
El `continue` no es tan usado y necesario, pero sirve para **evitar estrucuras anidadas** y hacer el **código más limpio si se tiene muchas condiciones**. 
En la practica no se utiliza tanto, incluso en ocaciones se prefiere evitarlo para mantener el flujo de control más explícito. Entonce sería útil cuando se tiene muchas condiciones y se quere evitar anidar `if`s. Por ejemplo un ejemplo en el cual sería bueno emplearlo sería:
```py
for user in users:
    if not user.is_active:
        continue
    if user.role != "admin":
        continue

    # solo admin activos llegan aquí
    print(f"{user.name} tiene acceso")
```
# C14: Argumentos arbitrarios (args)
En Python están los **argumentos arbitrarios** o **"args"**, se usa con asterisco `*` para capturar una **cantidad variable de argumentos posicionales** en una función:
```py
def print_texts(*text):
    print(text)
```
Aquí se lería: Esta función **puede recibir cualquier cantidad de argumentos** y todos **serán guardados en una tupla llama** `text`.
Ejemplo de entrada:
```py
print_texts("Python", "PHP", "Javascript")
```
Y el ejemplo de su salida:
```py
('Python', 'PHP', 'Javascript')
```
# C15: Constructor
El **constructor** de la clase se ejecuta automáticamente **cada vez** que se crea un objeto (una instancia) de esa clase:
```py
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

persona1 = Persona("Diego", 25)
print(persona1.nombre)  # Diego
```
`__init__` no es obligación su uso, se puede tener una clase sin ella si no se necesita inicializar atributos al momento de crear la instancia:
```py
class Mascota:
    def ladrar(self):
        print("Guau!")

perro = Mascota()
perro.ladrar()
```
Pero en cuento se necestia inicializar valores personalizados, como nombre, precio, edad, dirección, color, etc. **Sí se necesitará** `__init__`
> En otras palabras: El uso de `__init__` es **correcto y recomendable** cuando la clase necestia **inicializar atributos** al momento de crear una instancia.
# C16: Timedelta
En Python, `timedelta` es una clase del módulo `datetime` que representa una **diferencia de tiempo** entra dos fechas, horas o datetimes. Sirve para trabajar con intervalos temporales (ej: "5 días y 3 horas"), en lugar de representar una fecha o una hora concreta.
Es útil para:
- **Sumar o restar** días, horas, minutos, etc., a una fecha.
- **Calcular la diferencia** entre dos fechas/horas.
- **Medir duraciones** en programas (por ejemplo, cuánto tarda en ejecutarse algo).
- Evitar errores con cálculos manuales de fechas (meses con diferente número de días, años bisiestos, cambios de hora, etc.).
Lo más caracteristico es que `timedelta` funciona como una "moneda común" para sumar o restar intervalos de tiempo, **pero no con todos los tipos de fecha/hora de Python indiscriminadamente**
Un ejemplo básico sería:
```py
from datetime import datetime, timedelta

# Fecha actual
hoy = datetime.now()

# Crear un timedelta de 5 días
cinco_dias = timedelta(days=5)

# Sumar 5 días a la fecha actual
en_cinco_dias = hoy + cinco_dias
print("En 5 días será:", en_cinco_dias)

# Restar 5 días
hace_cinco_dias = hoy - cinco_dias
print("Hace 5 días fue:", hace_cinco_dias)
```
Aquí una tabla con la compatibilidad de fechas en Python:
| Operación                 | datetime                         | date                           | time          | timedelta                                |
| ------------------------- | -------------------------------- | ------------------------------ | ------------- | ---------------------------------------- |
| **datetime** ± datetime   | ➖ ✅ (`timedelta` como resultado) | ❌ `TypeError`                  | ❌ `TypeError` | ➕/➖ ✅ (`datetime` como resultado)        |
| **date** ± date           | ✅ (`timedelta` como resultado)   | ✅ (`timedelta` como resultado) | ❌ `TypeError` | ➕/➖ ✅ (`date` como resultado)            |
| **time** ± time           | ❌ `TypeError`                    | ❌ `TypeError`                  | ❌ `TypeError` | ❌ Directo (`time` no admite `timedelta`) |
| **timedelta** ± timedelta | ✅ (`timedelta` como resultado)   | ✅ (`timedelta` como resultado) | ❌ `TypeError` | ✅ (`timedelta` como resultado)           |
# C17: List Comprehensions
Son una **forma corta y elegante de crar listas** nuevas aplicando una expresión a cada elemento de un iterable (como una lista, tupla o rango) y opcionalmente filtrando elementos con una condición. En vez de utilizar un bucle `for` tradicional para contruir una lista, se puede hacer en una sola línea:
```py
[expresión for elemento in iterable if condición]
```
Esta sería la estrucura básica, lo que pasa en el ejemplo sería:
- `expresión` → Qué valor se va a colocar en la lista resultante (puede ser el elemento en sí o algo modificado).
- `elemento` → La variable que toma cada valor del iterable.
- `iterable` → La secuencia o colección sobre la que iteras.
- `if condición` (opcional) → Filtro para incluir solo los elementos que cumplan la condición.
Y ejemplo aplicable sería la creación de una lista de cuadrados:
```py
# Con List Comprehensions:
cuadrados = [x**2 for x in range(5)]
print(cuadrados)  # [0, 1, 4, 9, 16]

# Con un for:
cuadrados = []
for x in range(5):
    cuadrados.append(x**2)
```
s
# C18: Lambda
Es una forma corta de crar una **función anónima** (sin nombre) usando la palabra clave `lambda`. Sive cuando se necesita una función rápida y simple, normalmente en una sola línea, sin la formalidad de definiarla con `def`.
```py
lambda argumentos: expresión
```
- `argumentos` → Parámetros que recibe la función.
- `expresión` → Lo que la función devuelve (no se usa `return`, se devuelve automáticamente).
Un ejemplo simple en su uso sería:
```py
# Función tradicional
def cuadrado(x):
    return x**2

# Función lambda
cuadrado_lambda = lambda x: x**2

print(cuadrado_lambda(5))  # 25
```
# C19: Función de orden superior
Es una función que:
1. Recibe como argumento otra función
2. O devuelve otra función como resultado
3. (o ambas a la vez)
En Python las funciones son **ciudadanos de primera clase** (first-class citizens), significa que se puen pasar como parametros, guardarlas en variables, retornarlas, ect., igual que otro valor.
1. Ejmplo: Rebibir funciones como argumento:
```py
def aplicar(funcion, valor):
    return funcion(valor)

def cuadrado(x):
    return x * x

print(aplicar(cuadrado, 5))  # 25
```
Aquí `aplicar` es de orden superior porque recibe otra función (`cuadrado`) como parámetro.
2. Ejemplo: Devolver funciones:
```py
def multiplicador(n):
    def multiplicar(x):
        return x * n
    return multiplicar

por_dos = multiplicador(2)
print(por_dos(5))  # 10
```
`multiplicador` devuelve una nueva función, así que también es de orden superior.
3. Ejemplo integrados de Python
Muchas funciones integradas de Python son de orden superior:
- `sorted(iterable, key=func)`
- `filter(func, iterable)`
- `map(func, iterable)`
```py
nums = [1, 2, 3, 4, 5]
print(list(map(cuadrado, nums)))  # [1, 4, 9, 16, 25]
```
s
# C20: Función Cerrada (closure)
Es una función interna que **recuerda** y **puede acceder** a las varialbes de su función externa, incluso después de que la función externa haya terminado de ejecutarse. Es como si la función interna "llevara consigo" un pequeño paquete con las variables que tenía a su alrededor cuando fue creada.
Para que exista una **closure** deben cumplirse 3 cosas:
1. **Una función interna** definida dentro de otra función.
2. **La función interna usa variables** de la función externa.
3. **La función externa devuelve** la función interna, para que pueda ejecutarse después.
```py
def crear_saludador(nombre):
    def saludar():
        print(f"Hola, {nombre}")
    return saludar

saludo_a_aemon = crear_saludador("Aemon Targaryen")
saludo_a_aemon()  # Hola, Aemon Targaryen
```
Aquí ocurre lo siguiente:
- Cuando `crear_saludador` termina, su variables `nombre` normalmente debería desaparecer.
- Pero como `saludar` la necesita, Python **la "captura" y la guarda** junto con la función interna.
- Así, aunque `crear_saludador` ya acabó, `saludar` sigue recordando "`Aemon Targaryen"`
Las **closures** son muy útiles para:
- Crear funciones personalizadas con configuración previa (factories).
- Evitar variables globales.
- Encapsular datos para que no puedan modificarse desde fuera.
```py
def contador():
    cuenta = 0
    def incrementar():
        nonlocal cuenta
        cuenta += 1
        return cuenta
    return incrementar

mi_contador = contador()
print(mi_contador())  # 1
print(mi_contador())  # 2
print(mi_contador())  # 3
```
Aquí `cuenta` se mantiene entre llamadas, sin usar variables globales.
# C21: Built-in Higher Order Functions
Como se mencionó en *C19* están las **funciones de orden superior que ya vienen incluidas en el propio lenguaje** (las que trae en propio Python "de fabricaa", sin necesidad de importarlas).
Entonces una función de orden superior es una **funcion que recibe otra función como argumento** o **Deveulve otra función**.
Un ejemplo de built-in higher order functions:
- `map(func, iterable` Aquí aplica un función a cada elemento
```py
nums = [1, 2, 3, 4]
cuadrados = list(map(lambda x: x**2, nums))
print(cuadrados)  # [1, 4, 9, 16]
```
- `filter(func, iterable)` Filtra elementos que cumplen una condición.
```py
pares = list(filter(lambda x: x % 2 == 0, nums))
print(pares)  # [2, 4]
```
s
# C22: with + file
En Python cuando se trabaje con ficheros lo recomendable es siempre usar `with`.
Con `witch` se obtienen las siguientes ventajas:
- **Cierre automático del archivo**: No se necesita llamar a `close()`, Python lo hace por el usuario.
- **Manejo seguro de errores**: Si ocurre una excepción dentro del bloque, el archivo igualemnte se cierra.
- **Código más limpio y legible**: Menos líneas y más fácil de leer
Algunos ejemplos prácticos serían:
**Lectura:**
```py
with open("datos.txt", "r") as f:
    contenido = f.read()
```
**Escritura:**
```py
with open("salida.txt", "w") as f:
    f.write("Guardando información...\n")
```
**Copia de archivos (lectura + escritura):**
```py
with open("origen.txt", "r") as f_in, open("destino.txt", "w") as f_out:
    for linea in f_in:
        f_out.write(linea)
```
Hay casos en que no es necesario `with`, esto sería solo en situaciones muy especificas, por ejemplo:
- si se quiere **mantener un archivo abierto mucho tiempo** (ejemplo: un log que va a escribir línea por línea durante toda la ejecución).
- Si se **necesita abrir/cerrar manualmente en diferentes momentos** y no todo en un mismo bloque
# C23: Regular expressions
La **expresiones regulares** (regular expressions o regex) en Python son una forma muy poderosa de buscar extraer o manipular **patrones de texto** dentro de strings. 
Es similar a pensar en ellas como una especie de "mini busqueda" que permite decirle a Python:
- *“Encuentra todas las palabras que empiecen con mayúscula”*,
- *“Verifica si este correo tiene el formato correcto”*,
- *“Reemplaza todos los números de un texto por X”*.
Las regex se usan con el módulo incorporado `re`
```py
import re
```
Un ejemplo baso de uso sería buscar un patrón de un texto:
```py
import re

texto = "Mi número es 12345"
patron = r"\d+"   # \d significa "números", + significa "uno o más"
resultado = re.search(patron, texto)

print(resultado.group())  # 12345
```
# C24: Conexión a SQL (pyodbc)
En python se pueden hacer conexiones a distintas DBs de manera sencilla. Aquí se hace una conexión a SQL básico. Dentro de python hay 3 alternativas que son las más usadas:
- sqlite3: SQLite integrado
- pyodbc: Conexión SQL clásica
- SQLAlchemy: ORM / abstracción
*pyodbc* es una biblioteca (módulo) de código abierto para Python que **permite conectar aplicaciones Python a casi cualquier base de datos que utilice el estándar ODBC (Open Database Connectivity)**. Facilita la ejecución de consultas SQL, la recuperación de resultados y la gestión de transacciones con sistemas como SQL Server, Oracle, MySQL y PostgreSQL.
# C25: C25 raw string
En python puede ocurrir que cuando se utilize el simbolo de slash (/) en un string, python lo interprete cómo si fuera un comando, cómo puede ser: "/n", para evitar eso se puede utilizar "raw string".
Añadiendo la letra "r" al inicio, esto indicará que no se interprete un escape:
`r"SERVER=LAPTOP-QJ6643FR\DALPO;"`.
# C26: Reduce
La función `reduce()`, pertenece al modulo `functools`, aplica una función de manera acumulativa a los elementos de un iterable (como una lista), de izquierda a derecha, para condensarlos e un único valor. Distinto de `map()` o `filter()`. `reduce()` toma dos argumentos -Una función y un iterable- para procesar pares de elementos secuencialmente.
# C27:
# C28:
# C29:
# C30: