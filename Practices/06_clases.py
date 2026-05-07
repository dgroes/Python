#### Guitarras
class Guitarra:
    def __init__(self, marca, modelo, precio, cantidad_stock):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.cantidad_stock = cantidad_stock

    def info(self):
        return f"Marca: {self.marca}  {self.modelo}, Precio: {self.precio}, Cantidad en tienda: {self.cantidad_stock}"

g1 = Guitarra("Fender", "Telecaster", 1200, 14)
g2 = Guitarra("Guild", "Starfire II", 830, 5)
g3 = Guitarra("Cordoba", "Mini Traveler", 250, 10)
g4 = Guitarra("Gibson", "Les Paul Standard", 2500, 3)
g5 = Guitarra("Ibanez", "RG550", 900, 7)
g6 = Guitarra("Yamaha", "Pacifica 112V", 300, 20)
g7 = Guitarra("PRS", "SE Custom 24", 850, 4)
g8 = Guitarra("Epiphone", "Les Paul", 400, 12)
g9 = Guitarra("Gretsch", "G5420T Electromatic", 800, 6)
g10 = Guitarra("Squier", "Classic Vibe", 400, 15)
g11 = Guitarra("Fender", "Stratocaster", 1300, 10)
g12 = Guitarra("Gibson", "SG Standard", 2200, 2)
g13 = Guitarra("Ibanez", "RG450DX", 750, 8)
g14 = Guitarra("Yamaha", "Revstar RS502T", 600, 9)
g15 = Guitarra("PRS", "SE Custom 22", 800, 5)
g16 = Guitarra("Epiphone", "SG Special", 350, 11)
g17 = Guitarra("Gretsch", "G2622 Streamliner", 700, 7)
g18 = Guitarra("Squier", "Bullet Stratocaster", 200, 20)
g19 = Guitarra("Fender", "Mustang", 900, 6)
g20 = Guitarra("Gibson", "Flying V", 3000, 1)

coleccion_guitarras = [g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14, g15, g16, g17, g18, g19, g20]

def mostrar_guitarras(guitarras):
    for guitarra in guitarras:
        print(guitarra.info())

def guitarras_filtro_precio(guitarras, precio_minimo):
    for guitarra in guitarras:
        if guitarra.precio > precio_minimo:
            print(guitarra.info())

def buscar_marca(guitarras, marca_bucar):
    for guitarra in guitarras:
        if marca_bucar in guitarra.marca:
            print(guitarra.info())

# Calcular el Valor de guitarras por su Stock
def valor_inventario(guitarras):
    precio = 0
    for guitarra in guitarras:
        precio += guitarra.precio * guitarra.cantidad_stock
    print (f"${precio}")

def ordenar_por_valor(guitarras):
    guitarras_ordenadas = sorted(guitarras, key=lambda guitarra: guitarra.precio)

    for guitarra in guitarras_ordenadas:
        print(guitarra.info())


print("Mostrar Todas las guitarras")
mostrar_guitarras(coleccion_guitarras)

print("")
print("Gutarras sobre un precio")
guitarras_filtro_precio(coleccion_guitarras, 1000)

print("")
print("Buscar por marca")
buscar_marca(coleccion_guitarras, "Fender")

print("")
print("Valor del stock en tienda")
valor_inventario(coleccion_guitarras)

print("")
print("Ordenar guitarras por precio (menor a mayor)")
ordenar_por_valor(coleccion_guitarras)


#### Interaccion con Ficheros

fichero = open("fichero.txt", 'w')

for guitarra in coleccion_guitarras:
    fichero.write(guitarra.info() + "\n")
fichero.close()

#### Interaccion con DB