from random import randint
from os import system
system("cls")

productos = {1: [17431, "Ps5", "Consolas", 800000, 50],
            2: [12754, "Lenovo", "Computadoras", 850000, 25]}
ventas = {}
categorias = ("Computadoras", "Telefonos", "Consolas", "Televisores", "Electrodomesticos")


def registrar():
    system("cls")
    id = randint(10000, 150000)
    while True:
        nombre = input("Ingrese nombre del producto: ")
        if len(nombre) >= 3:
            nombre = nombre.capitalize()
            break
        else:
            print("Ingrese un nombre valido")
    while True:
        categoria = input("Ingrese categoria (Computadoras, Telefonos, Consolas, Televisores, Electrodomesticos): ")
        categoria = categoria.capitalize()
        if categoria in categorias:
            break
        else:
            print("Ingrese una categoria valida")
    while True:
        precio = input("Ingrese el precio del producto: ")
        if precio.isnumeric():
            precio = int(precio)
            if precio > 0:
                break
        else:
            print("Ingrese un precio valido")
    while True:
        stock = input("Ingrese el stock del producto: ")
        if stock.isnumeric():
            stock = int(stock)
            if stock > 0:
                break
        else:
            print("Ingrese un stock valido")
    key = len(productos)
    key += 1
    productos[key] = [id, nombre, categoria, precio, stock]

def listar():
    system("cls")
    if len(productos) == 0:
        print("No hay productos registados")
        return
    else:
        print("ID   | Nombre     | Categoría    | Precio     | Cantidad")
        for i, producto in productos.items():
            print(f"""---------------------------------------------------------
{producto[0]} | {producto[1]} | {producto[2]}  | {producto[3]}  | {producto[4]}""")

def imprimir():
    system("cls")
    if len(productos) == 0:
        print("No hay productos registrados")
        return
    while True:
        op = input("Desea imprimir por categoria (Computadoras, Telefonos, Consolas, Televisores, Electrodomesticos) o todos: ")
        op = op.capitalize()
        if op in categorias or op == "Todos":
            break
        else:
            print("Ingrese una opcion valida")
    archivo = open("Inventario.csv", "w")
    archivo.write("ID;Nombre;Categoría;Precio;Cantidad\n")
    for i, producto in productos.items():
        if op == producto[2]:
            archivo.write(f"{producto[0]};{producto[1]};{producto[2]};{producto[3]};{producto[4]}\n")
        elif op == "Todos":
            archivo.write(f"{producto[0]};{producto[1]};{producto[2]};{producto[3]};{producto[4]}\n")
    archivo.close()

def realizar_venta():
    system("cls")
    if len(productos) == 0:
        print("No hay productos para vender")
        return
    else:
        


while True:
    op = input("""
Bienvenido a PC Factory
1.- Registrar producto
2.- Listar productos
3.- Imprimir informe de inventario
4.- Realizar venta
0.- Salir

Eliga opción: """)
    match op:
        case "1":
            registrar()
        case "2":
            listar()
        case "3":
            imprimir()
        case "4":
            pass
        case "0":
            print("Saliendo...")
            break
        case other:
            print("Ingrese una opcion valida")