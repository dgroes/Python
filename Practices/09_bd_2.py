from datetime import datetime

## Conexión a la BD
import pyodbc
import os

conexion = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    r"SERVER=LAPTOP-QJ6643FR\DALPO;" # C25 raw string
    "DATABASE=python_test;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;",
)


## Clase
class Cliente:
    def __init__(self, nombre, apellido, email, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
    
    def info(self):
        print(f"Nombre: {self.nombre}, Apellido: {self.apellido}, Email: {self.email}, Teléfono: {self.telefono}")
    

## Creación de la tabla "cliente"
def crear_tabla_cliente():
    cursor = conexion.cursor()

    query = """
        IF NOT EXISTS (
            SELECT *
            FROM sys.tables
            WHERE name = 'cliente'
        )
        BEGIN
            CREATE TABLE cliente(
                id INT IDENTITY(1,1) PRIMARY KEY,
                codigo VARCHAR(15),
                nombre VARCHAR (50),
                apellido VARCHAR (50),
                email VARCHAR(100),
                telefono VARCHAR(9)
            )
        END

    """

    cursor.execute(query)
    conexion.commit()
    print("Tabla creada")

#crear_tabla_cliente()


def crear_cliente(nombre, apellido, email, telefono):
    try:
        cursor = conexion.cursor()

        query_email = "SELECT * FROM cliente WHERE email = ?"
        consulta = cursor.execute(query_email, email)
        filas = consulta.fetchall()
        #for fila in filas:
        #    print(fila)
        conexion.commit()


        if filas:
            print("Ya existe un usuario registrado con ese correo 🐀")
        else:
            query = """
                INSERT INTO cliente (nombre, apellido, email, telefono, codigo) 
                VALUES(?, ?, ? ,?, ?)
                """
            now = datetime.now()
            codigo = str(now.strftime("%Y%m%d%H%M%S"))
            
            cursor.execute(query, nombre, apellido, email, telefono, codigo)
            conexion.commit()

            print(f"Se creó el cliente {nombre}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()


def ver_clientes():
    try:
        cursor = conexion.cursor()

        query = "SELECT * FROM cliente"
        cursor.execute(query)

        for row in cursor.fetchall():
            print(row)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

def editar_email(email, codigo):
    try:
        cursor = conexion.cursor()
        query = "UPDATE c SET c.email = ? FROM cliente c WHERE c.codigo = ?"

        cursor.execute(query, email, codigo)
        conexion.commit()

        print(f"Cliente {codigo} editado")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

def eliminar_cliente(codigo):
    try:
        cursor = conexion.cursor()

        query = "DELETE FROM cliente WHERE codigo = ?"

        cursor.execute(query, codigo)
        conexion.commit()
        print(f"Cliente '{codigo}' eliminado de la BD 🗑️")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()


## Eportación a un TXT
def exportar_clientes():
    try:
        cursor = conexion.cursor()
        query = "SELECT * FROM cliente"
        result = cursor.execute(query)
        clientes = result.fetchall()

        with open("Files_to_practices/clientes.txt", 'w') as file:
            for cliente in clientes:
                file.write(
                    f"{cliente}\n"
                )

        print("Clientes exportados👍")
    
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

def importar_clientes():
    fichero = "Files_to_practices/importar_clientes.txt"
    clientes = []
    contador = 0

    try:
        cursor = conexion.cursor()

        with open (fichero, 'r') as file:
            for line in file:
                
                now = datetime.now()
                codigo = str(now.strftime("%Y%m%d%H%M%S"))


                data_parts = line.strip().split(',')

                clientes.append(data_parts)


                nombre = clientes[contador][0]
                apellido = clientes[contador][1]
                email = clientes[contador][2]
                telefono = clientes[contador][3]    

                query = """INSERT INTO cliente (nombre, apellido, email, telefono, codigo) 
                    VALUES(?, ?, ? ,?, ?)
                    """
                cursor.execute(query, nombre, apellido, email, telefono, codigo)            
                
                contador += 1

            print(f"[EXITO] {contador} clientes imporatos con exito 🚚" )
        conexion.commit()

    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
#crear_cliente("qwerty", "suyy", "mansu@gmail.com", "744990615")





def programa():
    respuesta = 0

    def clear_terminal():
        # 'nt' is Windows, everything else (posix) is Linux/macOS
        os.system('cls' if os.name == 'nt' else 'clear')

    while respuesta != "7":
        print("**********Clientes**********")
        print("OPCIONES DE PROGRAMA")

        opciones = """
            [1] Ver Clientes 🔍
            [2] Crear Cliente 👤
            [3] Eliminar Cliente 🗑️
            [4] Editar Email ✏️
            [5] Exportar Cliente 🚚
            [6] Importat Cliente 📦
            [7] CERRAR PROGRAMA 🏃🚪
            """

        print(opciones)
        respuesta = input("Elija acción: ")

        if respuesta == "7":
            print("Chaito 👋")
            break
        elif respuesta == "1":
            clear_terminal()
            print("\n [1] VER CLIENTES 🔍")
            ver_clientes()

        elif respuesta == "2":
            clear_terminal()
            print("\n [2] CREAR NUEVO CLIENTE 👤")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            email = input("Email: ")
            telefono = input("Teléfono: ")

            crear_cliente(nombre, apellido, email, telefono)
            print(f"Cliente {nombre} cread con exito")

        elif respuesta == "3":
            clear_terminal()
            print("\n [3] Eliminar Cliente 🗑️")
            codigo = input("Código de cliente a eliminar: ")

            eliminar_cliente(codigo)

        elif respuesta == '4':
            clear_terminal()
            print("\n [4] Editar Email ✏️")
            codigo = input("Código del cliente a editar: ")
            email = input("Nuevo email: ")
            editar_email(email, codigo)

        elif respuesta == '5':
            clear_terminal()
            print("\n [5] Exportar Cliente 🚚")
            exportar_clientes()

        elif respuesta == '6':
            clear_terminal()
            print("\n [6] Importat Cliente 📦")
            importar_clientes()



programa()

#importar_clientes()

#exportar_clientes()
#eliminar_cliente("20260508003200")
#ver_clientes()  
# seditar_email("putero_nato@gmail.com", "20260508003247")
