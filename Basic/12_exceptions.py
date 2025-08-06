# Excepciones Handling

first_number = 1
# second_number = 4
second_number = "4"

# Try except
try:
    print(first_number + second_number)
    print("[OK] Operación ejecutada exitosamente ⚡")
except:
    print("[Error] Se ha producido un error, no se pudo ejecutar la operación 💥")


print("--------")

# Try excep Else
# El Else se ejecuta cuandon entre el try y
# except no se ha producido un error(excepción)
try:
    print(first_number + second_number)
    print("[OK] Operación ejecutada exitosamente ⚡")
except:
    print("[Error] Se ha producido un error, no se pudo ejecutar la operación 💥")
else:
    print("[Else] La ejecución continúa correctamente ✔️")

print("--------")


# Finally
# Finally se ejecuta cuando haya o no haya una excepción

try:
    print(first_number + second_number)
    print("[OK] Operación ejecutada exitosamente ⚡")
except:
    print("[Error] Se ha producido un error, no se pudo ejecutar la operación 💥")
else:
    print("[Else] La ejecución continúa correctamente ✔️")
finally:  # Opcional
    print("[Finally] La ejecución ha finalizado 👌")


print("--------")
# Excepciones por tipo
user_input = input("Ingresa un número entero: ")

try:
    number = int(user_input)
    print(f"[OK] Ingresaste un número entero (int). Tu número es: {number}")
except ValueError:
    print("[Error: ValueError]: No ingresaste un número entero válido.")



print("--------")
# Captura de la información de la excepción
user_input = input("Ingresa un número entero: ")

try:
    number = int(user_input)
    print(f"[OK] Ingresaste un número entero (int). Tu número es: {number}")
except ValueError as e:
    print(f"[Error: ValueError]: No ingresaste un número entero válido -> {e}.")
except Exception as e:
    print(e)
# except Exception es una captura general de errores. Equivale a un `except` vacío pero mejor