from os import system
system("cls")

productos = [
    {'Nombre': 'Chocolate', 'Categoria': 'Alimento', 'Precio': 1400, 'Stock': 30},
    {'Nombre': 'Poleron', 'Categoria': 'Ropa', 'Precio': 21990, 'Stock': 20},
    {'Nombre': 'Monitor', 'Categoria': 'Electronica', 'Precio': 149990, 'Stock': 5}
]

categorias = ["Electronica", "Ropa", "Alimento"]

def registrar():    #Registrar producto
    system("cls")
    nombre = input("Ingrese el nombre del producto: ")
    categoria = input("Ingrese la categoria del producto: ")
    while True:
        if categoria in categorias:
            break
        else:
            print("Ingrese una categoria valida")
            categoria = input("Ingrese la categoria del producto: ")
    precio = int(input("Ingrese un precio al producto: "))
    while True:
        if precio <= 0:
            print("Ingrese un precio valido")
            precio = int(input("Ingrese un precio al producto: "))
        else:
            break
    stock = int(input("Ingrese el stock: "))
    while True:
        if stock <= 0:
            print("Ingrese una cantidad valida")
            stock = int(input("Ingrese el stock: "))
        else:
            break
    nuevo_producto = {
        'Nombre': nombre,
        'Categoria': categoria,
        'Precio': precio,
        'Stock': stock
    }
    productos.append(nuevo_producto)
    print(F"{nombre} registrado con exito!")

def listar():
    system("cls")
    for producto in productos:
        for clave, valor in producto.items():
            print(f"{clave}: {valor}")
        print("-----")

def informe():
    system("cls")
    print("-" * 30)
    print("INFORME DE INVENTARIO")
    print("-" * 30)
    for producto in productos:
        print(f"Nombre: {producto['Nombre']}")
        print(f"Categoría: {producto['Categoria']}")
        print(f"Precio: ${producto['Precio']}")
        print(f"Stock: {producto['Stock']}")
        print("-" * 30)



while True:
    print("""
1. Registrar producto
2. Lista todos los productos
3. Imprimir informe de inventario
0. Salir del programa
""")
    
    op = input("Elegir opción: ")
    match op:
        case "1":   #Registrar producto
            registrar()
        case "2":   #Lista de productos
            listar()
        case "3":   #Imprimir informe
            informe()
        case "0":   #Salir
            print("Saliendo...")
            input("pulse un boton para continuar")
            break
        case other:
            print("Opcion invalida")