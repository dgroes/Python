def tareas_pendientes(file):
    contador = 1
    with open(file, "r", encoding="utf-8") as tasks:
        for line in tasks:
            print(f"{contador}. {line.strip()}")
            contador += 1


def añadir_tarea(file):
    with open(file, "a", encoding="utf-8") as tasks:
        while True:
            new_task = input("Ingrese la nueva tarea: ")
            tasks.write("\n")
            tasks.write(new_task)

            continuar = input("¿Desea agregar otra tarea? (s/n): ").lower()
            if continuar != "s":
                break


# tareas_pendientes("./Files_to_practices/03_tareas.txt")
añadir_tarea("./Files_to_practices/03_tareas.txt")
