class VideoJuego:
    def __init__(self, titulo, genero, precio, stock):
        self.titulo = titulo
        self.genero = genero
        self.precio = precio
        self.stock = stock

    def info(self):
        return f"Titulo: {self.titulo}, Genero: {self.genero}, Precio: {self.precio}, Stock: {self.stock} "

v1 = VideoJuego("The Legend of Zelda: Breath of the Wild", "Aventura", 59.99, 10)
v2 = VideoJuego("Super Mario Odyssey", "Plataformas", 49.99, 15)
v3 = VideoJuego("Red Dead Redemption 2", "Acción", 39.99, 5)
v4 = VideoJuego("The Witcher 3: Wild Hunt", "RPG", 29.99, 8)
v5 = VideoJuego("Minecraft", "Sandbox", 19.99, 20)
v6 = VideoJuego("Fortnite", "Battle Royale", 0.00, 100)
v7 = VideoJuego("Call of Duty: Modern Warfare", "FPS", 59.99, 12)
v8 = VideoJuego("Among Us", "Multijugador", 4.99, 50)
v9 = VideoJuego("Cyberpunk 2077", "RPG", 49.99, 7)
v10 = VideoJuego("Animal Crossing: New Horizons", "Simulación", 59.99, 18)
v11 = VideoJuego("Hades", "Roguelike", 24.99, 10)
v12 = VideoJuego("Apex Legends", "Battle Royale", 0.00, 100)
v13 = VideoJuego("Genshin Impact", "RPG", 0.00, 100)
v14 = VideoJuego("Valorant", "FPS", 0.00, 100)
v15 = VideoJuego("League of Legends", "MOBA", 0.00, 100)
v16 = VideoJuego("Overwatch", "FPS", 39.99, 15)
v17 = VideoJuego("Doom Eternal", "FPS", 59.99, 8)
v18 = VideoJuego("The Elder Scrolls V: Skyrim", "RPG", 29.99, 10)
v19 = VideoJuego("Grand Theft Auto V", "Acción", 29.99, 20)
v20 = VideoJuego("Dark Souls III", "RPG", 49.99, 5)

videojuegos = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20]

# Guardar juegos en un fichero
def guardar_videojuegos(videojuegos):
    # Crear fichero
    f = open("videojuegos.txt", "w")
    for videojuego in videojuegos:
        f.write(videojuego.info() + "\n")
    f.close()

guardar_videojuegos(videojuegos)


leer = "videojuegos.txt"

def leer_videojuegos(archivo):
    f = open(archivo, "r")
    
    for linea in f:
        print(linea)

    f.close()

def contar_videojuegos(archivo):
    with open(archivo, "r") as f:
        row_count = sum(1 for line in f)
    return row_count


def buscar_videojuego(texto, fichero):
    with open(fichero, 'r') as file:
        for line in file:
            if texto in line:
                print(f"Coincidencias: {line.strip()}")


""" def agregar_videojuego(titulo, genero, precio, stock, fichero):
    with open(fichero, "a") as file:
        file.write(f"Titulo: {titulo}, Genero: {genero}, Precio: {precio}, Stock: {stock}")
 """

def guardar_juegos_gratis(fichero):
    with open (fichero, 'r') as file:
        for line in file:
            if "0.0" in line:
                with open("free_to_play.txt", "a") as free:
                    free.write(f"{line.strip()}" + "\n")
                


def vaciar_fichero(fichero):
    open (fichero, "w").close()


# bonus (logs)
from datetime import datetime

def agregar_videojuego(titulo, genero, precio, stock, fichero):

    with open(fichero, "a") as file:
        file.write(
            f"\nTitulo: {titulo}, Genero: {genero}, Precio: {precio}, Stock: {stock}"
        )

    with open("logs.txt", "a") as log:

        fecha = datetime.now()

        log.write(
            f"[{fecha}] Juego agregado: {titulo}\n"
        )


leer_videojuegos(leer)

print(f"Hay {contar_videojuegos(leer)} Videojuegos")

print(" ")
buscar_videojuego("Apex", leer)

print(" ")
agregar_videojuego("Terraria", "Aventura", 9.99, 12, leer)


guardar_juegos_gratis(leer)

# vaciar_fichero(leer)