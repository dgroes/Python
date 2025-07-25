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
# C06:
# C07:
# C08:
# C09:
# C010:
# C011: