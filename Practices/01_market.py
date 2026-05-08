products = {
    0: {"Nombre": "Bebida", "Precio": 1200},
    1: {"Nombre": "Hamburguesa", "Precio": 2500},
    2: {"Nombre": "Papas Fritas", "Precio": 800},
    3: {"Nombre": "Ensalada", "Precio": 1500},
    4: {"Nombre": "Postre", "Precio": 1000},
    5: {"Nombre": "Pizza", "Precio": 3000},
    6: {"Nombre": "Sopa", "Precio": 900},
    7: {"Nombre": "Taco", "Precio": 2000},
    8: {"Nombre": "Sushi", "Precio": 3500},
    9: {"Nombre": "Burrito", "Precio": 2200},
    10: {"Nombre": "Galleta", "Precio": 500},
    11: {"Nombre": "Batido", "Precio": 1800},
    12: {"Nombre": "Tarta", "Precio": 1600},
    13: {"Nombre": "Wrap", "Precio": 2400},
    14: {"Nombre": "Café", "Precio": 700},
    15: {"Nombre": "Té", "Precio": 600},
}

print(len(max(["diego", "diegods"])))


def ver_productos(products):
    print("|ID| Producto Precio")
    for index, product in products.items():
        print(f"|{index}| {product['Nombre']}: {product['Precio']}")


ver_productos(products)


def comprar_productos(products):
    print("--------------------------------------")
    print("-------------Buenas Tardes------------")
    print("    Por favor, introduzca el ID de    ")
    print("        los producto a comprar        ")
    print("")
    my_products = dict()
    id_product = input("Que producto desea agregar a su carrito? introduzca el ID: ")
    for id in products:
        if id_product == id:
            print("hol")

    print(id)
comprar_productos(products)
