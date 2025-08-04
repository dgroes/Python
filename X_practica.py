print("Practica Python 01")

# Lista de productos a comprar
store = {
    0: {"Producto": "Lasaña", "Precio": 4200},
    1: {"Producto": "Arroz 1K", "Precio": 1200},
    2: {"Producto": "Tomates 1/2K", "Precio": 780},
    3: {"Producto": "Pan 1K", "Precio": 980},
    4: {"Producto": "Capsulas de café", "Precio": 1320},
    5: {"Producto": "Pistola 9m", "Precio": 110000},
    6: {"Producto": "Arena para gato 10K", "Precio": 16000},
    7: {"Producto": "Corazones de pollo", "Precio": 2340},
    8: {"Producto": "Botella de agua", "Precio": 1380},
    9: {"Producto": "Bolsa de maní", "Precio": 1150},
    10: {"Producto": "Hamburgesa de pollo", "Precio": 990},
    11: {"Producto": "Juego de mesa", "Precio": 23000},
    12: {"Producto": "Libro generico", "Precio": 10050},
    13: {"Producto": "Aspirina", "Precio": 1150},
    14: {"Producto": "Pasta de dientes", "Precio": 3600},
    15: {"Producto": "Talco para pies", "Precio": 2160},
}
print("-----Supermercado Dalpo el Guapo 🐈-----")
print("*********Listado de productos***********")

for id, product in store.items():
    print("|" f"ID: {id}")
    for key, value in product.items():
        print("|" f"{key} : {value}")
    print("|---------------------------|")


# input("Desea agrega más productos? (si / no): ")
