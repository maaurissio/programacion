import random
from os import system

pedidos = []

sectores = ("Concepción", "Chiguayante", "Talcahuano", "Hualpén", "San Pedro")

def registro_pedido(pedidos):
    system("cls")
    disp_6 = 0
    disp_10 = 0
    disp_20 = 0
    id = random.randint(1, 100000)
    while True:
        nombre = input("Ingrese su nombre: ")
        if len(nombre) > 3 and nombre.isalpha():
            break
        else:
            print("Ingrese un nombre valido")
    while True:
        apellido = input("Ingrese su apellido: ")
        if len(apellido) > 3 and apellido.isalpha():
            break
        else:
            print("Ingrese un apellido valido")
    while True:
        direccion = input("Ingrese su direccion: ")
        if len(direccion) > 3:
            break
        else:
            print("Ingrese un apellido valido")

    while True:
        sector = input("1.-Concepcion\n2.-Chiguayante\n3.-Talcahuano\n4.-Hualpen\n5.-San Pedro\nEscoga su sector: ")
        match sector:
            case "1":
                sector = "Concepción"
                break
            case "2":
                sector = "Chiguayante"
                break
            case "3":
                sector = "Talcahuano"
                break
            case "4":
                sector = "Hualpen"
                break
            case "5":
                sector = "San Pedro"
                break
            case other:
                print("Por favor, ingrese una opcion valida")
    while True:
        litros = input("1.- Dispensador de 6 litros\n2.- Dispensador de 10 litros\n3.- Dispensador de 20 litros\nCual dispensador quiere: ")
        if litros == "1":
            cantidad = input("Ingrese la cantidad que desee: ")
            if cantidad.isnumeric():
                cantidad = int(cantidad)
                if cantidad > 0:
                    disp_6 += cantidad
                    op = input("Desea agregar mas dispensadores? s/n: ")
                    if op == "s":
                        continue
                    elif op =="n":
                        break
            else:
                print("Ingrese una cantidad valida")
        if litros == "2":
            cantidad = input("Ingrese la cantidad que desee: ")
            if cantidad.isnumeric():
                cantidad = int(cantidad)
                if cantidad > 0:
                    disp_10 += cantidad
                    op = input("Desea agregar mas dispensadores? s/n: ")
                    if op == "s":
                        continue
                    elif op =="n":
                        break
            else:
                print("Ingrese una cantidad valida")
        if litros == "3":
            cantidad = input("Ingrese la cantidad que desee: ")
            if cantidad.isnumeric():
                cantidad = int(cantidad)
                if cantidad > 0:
                    disp_20 += cantidad
                    op = input("Desea agregar mas dispensadores? s/n: ")
                    if op == "s":
                        continue
                    elif op =="n":
                        break
            else:
                print("Ingrese una cantidad valida")
        else:
            print("Ingrese una opcion valida")
            continue
    print("Pedido realizado exitosamente!")
    pedido = {
        "ID pedido": id,
        "Nombre": nombre,
        "Apellido": apellido,
        "Direccion": direccion,
        "Sector": sector,
        "Disp.6lts": disp_6,
        "Disp.10lts": disp_10,
        "Disp.20lts": disp_20
    }
    pedidos.append(pedido)

def listar(pedidos):
    system("cls")
    print("ID pedido        Cliente         Direccion       Sector      Disp.6lts       Disp.10lts      Disp.20lts")
    for pedido in pedidos:
        print(f"""
        {pedido["ID pedido"]}       {pedido["Nombre"]}      {pedido["Direccion"]}       {pedido["Sector"]}      {pedido["Disp.6lts"]}        {pedido["Disp.10lts"]}       {pedido["Disp.20lts"]}
                                    {pedido["Apellido"]}""")

def imprimir_ruta(pedidos):
    system("cls")
    sector_buscado = input("Ingrese un sector para imprimir (Concepción, Chiguayante, Talcahuano, Hualpén, San Pedro): ")
    if sector_buscado in sectores:
        archivo = open(f"pedido.csv", "w")
        archivo.write("IDpedido;Nombre;Apellido;Direccion;Sector;Disp.6lts;Disp.10lts;Disp.20lts")
        for pedido in pedidos:
            archivo.write(f"\n{pedido["ID pedido"]};{pedido["Nombre"]};{pedido["Apellido"]};{pedido["Direccion"]};{pedido["Sector"]};{pedido["Disp.6lts"]};{pedido["Disp.10lts"]};{pedido["Disp.20lts"]}\n")
        archivo.close()
    return

def buscar_pedido(pedidos):
    system("cls")
    while True:    
        id_buscado = input("Ingrese el ID del pedido que desea buscar: ")
        if id_buscado.isnumeric():
            id_buscado = int(id_buscado)
            break
        else:
            print("Ingrese un ID valido")
    for pedido in pedidos:
        if pedido["ID pedido"] == id_buscado:
            print(f"""ID pedido     Cliente     Direccion       Sector      Disp.6lts       Disp.10lts      Disp.20lts
        {pedido["ID pedido"]}       {pedido["Nombre"]}      {pedido["Direccion"]}       {pedido["Sector"]}      {pedido["Disp.6lts"]}        {pedido["Disp.10lts"]}       {pedido["Disp.20lts"]}
                                    {pedido["Apellido"]}""")
            return
    print("ID incorrecto o no existente")
