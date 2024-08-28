from os import system
system("cls")

productos = {}
#pedidos = {1: [["Pato", "pato@deus.cl", "Subfusil", 2, 1000000, 2000000]]}
pedidos = {}
categorias = ("Herramienta", "Material", "Electricidad")

def registrar_producto():
    system("cls")
    while True:
        nombre = input("Ingrese nombre del producto: ")
        if len(nombre) >= 3:
            break
        else:
            print("Ingrese un nombre valido")
    while True:
        categoria = input("Ingrese categoria del producto(Herramienta, Material, Electricidad): ")
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
    productos[key] = [nombre, categoria, precio, stock]

def listar():
    system("cls")
    if len(productos) == 0:
        print("No hay productos disponibles")
        return
    else:
        for i, producto in productos.items():
            print(f"""
                Nombre: {producto[0]}
                Categoria: {producto[1]}
                Precio: {producto[2]}
                Stock: {producto[3]}""")

def realizar_pedido():
    system("cls")
    if len(productos) == 0:
        print("No hay productos disponibles")
        return
    while True:
        nombre = input("Ingrese su nombre: ")
        if len(nombre) > 3:
            break
        else:
            print("Ingrese un nombre valido")
    while True:
        correo = input("Ingrese su correo: ")
        arroba, punto = correo.count("@"), correo.count(".")
        if arroba == 1 and punto == 1:
            break
        else:
            print("Ingrese un correo valido")
    
    listar()
    comprando = True
    pedido_total = []
    while comprando:
        producto_a_buscar = input("Ingrese el nombre del producto: ")
        while True:
            for i, producto in productos.items():
                if producto_a_buscar == producto[0]:
                    cantidad_a_pedir = int(input("Ingrese la cantidad que desea: "))
                    if cantidad_a_pedir <= producto[3]:
                        stock_nuevo = producto[3] - cantidad_a_pedir
                        producto[3] = stock_nuevo
                        total_pedido = cantidad_a_pedir * producto[2]
                        pedido_total.append([nombre, correo, producto_a_buscar, cantidad_a_pedir, producto[2], total_pedido])
                    else:
                        print("No hay stock suficiente")
                        pass
            op = input("Desea otro producto? s/n: ")
            if op == "s":
                break
            else:
                comprando = False
                break
    key = len(pedidos)
    key += 1
    pedidos[key] = pedido_total
    pedido_total = []

def exportar():
    system("cls")
    if len(pedidos) == 0:
        print("No hay pedidos disponibles")
        return
    else:
        archivo = open("pedido.csv", "w")
        archivo.write("Nombre;Correo;Producto;Stock;PrecioxU;PrecioTotal\n")
        for i, pedido in pedidos.items():
            for p in pedido:
                archivo.write(f"{p[0]};{p[1]};{p[2]};{p[3]};{p[4]};{p[5]}\n")
        archivo.close()


while True:
    opcion = input("""
1.- Registrar producto
2.- Listar productos
3.- Realizar pedido
4.- Exportar pedido
0.- Salir

Eliga opcion: """)
    match opcion:
        case "1":
            registrar_producto()
        case "2":
            listar()
        case "3":
            realizar_pedido()
        case "4":
            exportar()
        case "0":
            print("Saliendo...")
            break
        case other:
            system("cls")
            print("Por favor, escoga una opcion valida")