from os import system
system("cls")

# productos = []

productos = [["Chocolate", "Alimento", "1.500", "30"], ["Refrigerador", "Electronica", "250.000", "5"], ["Polera", "Ropa", "10.000", "10"]]

categoria = ["Electronica", "Ropa", "Alimento"]

def registrar():    #Registrar producto
    nombre = input("Ingrese nombre del producto: ")
    print(f"Dispone de tres categorias para el producto: {categoria}")
    categ = input("Ingrese categoria del producto: ")
    while categ not in categoria:
        categ = input("Ingrese una categoria valida: ")
    precio = input("Inrese el precio del producto: ")
    cantidad = input("Ingrese la cantidad en stock del producto: ")
    producto = [nombre, categ, precio, cantidad]
    productos.append(producto)
    return productos

def listar():
    print(productos)

def informe():
    op = input("Ingrese la categoria que desea imprimir: ")
    while op not in categoria:
        op = input("Ingrese una categoria valida: ")
    for i in productos:
        if i[1] == op:
            print(i)

while True:
    print("""
1. Registrar producto
2. Lista todos los productos
3. Imprimir informe de invenario
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