# C24: Conexión a SQL (pyodbc)
import pyodbc
from datetime import datetime

conexion = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    r"SERVER=LAPTOP-QJ6643FR\DALPO;" # C25 raw string
    ##"DATABASE=python;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;",
    ##autocommit=True
)

print("Conexión exitosa")


cursor = conexion.cursor()

# Ver todas las BD del servidor
""" cursor.execute("SELECT name FROM sys.databases")

for fila in cursor.fetchall():
    print(fila) """

# Creación de una DB, si no existe
cursor.execute("IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'python_test') CREATE DATABASE python_test")
conexion.commit()

# Creación de tablas
cursor.execute("USE python_test")
cursor.execute("""
    IF NOT EXISTS (
        SELECT *
        FROM sys.tables
        WHERE name = 'producto'
    )
    BEGIN
        CREATE TABLE producto (
            id INT IDENTITY(1,1) PRIMARY KEY,
            codigo VARCHAR(10),
            nombre VARCHAR(100)
        )
    END

    IF NOT EXISTS (
        SELECT *
        FROM sys.tables
        WHERE name = 'cliente'
    )
    BEGIN
        CREATE TABLE cliente (
            id INT IDENTITY(1,1) PRIMARY KEY,   
            codigo VARCHAR(10),
            nombre VARCHAR(60),
            apellido VARCHAR(60)
        )
    END

""")
conexion.commit()


# Modificar una tabla (Añadir nueva columna):
cursor.execute("""

IF NOT EXISTS (
    SELECT *
    FROM sys.columns
    WHERE name = 'stock'
    AND object_id = OBJECT_ID('producto')
)
BEGIN
    ALTER TABLE producto
    ADD stock INT
END

""")
conexion.commit()


def nuevo_producto(nombre, stock):

    try:

        cursor = conexion.cursor()

        sql = "SELECT COUNT(*) FROM producto"
        cursor.execute(sql)

        cantidad = cursor.fetchone()[0]
        fecha = datetime.now()
        codigo = str(cantidad) + str(len(nombre)) + str(fecha.year) + str(fecha.day)
        #codigo = fecha.strftime("%Y%m%d%H%M%S")
        print(codigo)
        sql = """
        INSERT INTO producto (nombre, codigo, stock)
        VALUES (?, ?, ?)
        """

        cursor.execute(sql, nombre, codigo, stock)
        conexion.commit()

        print(f"Producto {nombre} insertado con éxito!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()


def ver_productos():
    try:
        cursor = conexion.cursor()
        sql = "SELECT * FROM producto"
        cursor.execute(sql)
        
        resultado = cursor.fetchall()

        for fila in resultado:
            print(f"{fila}")

    except Exception as e:
        print (f"Error: {e}")
    finally:
        cursor.close()

def eliminar_producto(codigo):
    try:
        cursor = conexion.cursor()
        sql = "DELETE FROM producto WHERE codigo = (?)"

        cursor.execute(sql,codigo)
        conexion.commit()
        print(f"Producto '{codigo}' eliminado")

    except Exception as e:
        print (f"Error: {e}")
    finally:
        cursor.close()

def editar_producto(nombre, codigo):
    try:
        cursor = conexion.cursor()
        sql = "UPDATE p SET p.nombre = ? FROM producto p WHERE p.codigo = ?"

        cursor.execute(sql, nombre, codigo)
        conexion.commit()
        print(f"Producto {codigo} editado")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

## nuevo_producto("IdeaPad Slim 3 8va Gen", 5)
## eliminar_producto("672026")
ver_productos()
##editar_producto("Acer Nitro 5", "121120267")