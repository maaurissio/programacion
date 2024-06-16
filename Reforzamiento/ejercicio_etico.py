from os import system
system("cls")

# blacklist = []
blacklist = [["ignasio", "bustos"], ["maurisio", "pajardo"]]

def agregar(blacklist): #Agregar Veneco
    nombre = input("Ingrese el nombre del veneco: ")
    apellido = input("Ingrese el apellido del veneco: ")
    veneco = [nombre, apellido]
    blacklist.append(veneco)
    print("Veneco agregado")
    system("cls")

def fusilar(blacklist): #Eliminar Veneco
    veneco_fusilado = input("Ingrese el nombre del veneco que quiere fusilar: ")
    for ven in blacklist:
        if ven[0] == veneco_fusilado:
            print("Veneco fusilado")
            blacklist.remove(ven)
            return ven
    else:
        print("Ese veneco no esta en la lista")

def buscar(blacklist):  #Buscar Veneco
    veneco_buscado = input("Ingrese el veneco que quiere buscar: ")
    for ven in blacklist:
        if ven[0] == veneco_buscado:
            print(f"El veneco {ven[0]} si se encuentra en lista")
            return ven
        else:
            print(f"El veneco {ven[0]} no se encuentra en lista")

while True:
    print(blacklist)
    print("""
    BIENVENIDO A VEGA MONUMENTAL
    1. Agregar Venecos
    2. Fusilar Venecos
    3. Buscar Veneco
    0. Salir
""")
    op = input("Seleccione opción: ")

    if op == "1":   # Agregar
        agregar(blacklist)
    elif op =="2":  # Eliminar
        fusilar(blacklist)
    elif op == "3": # Buscar
        buscar(blacklist)
    elif op == "0": # Salir
        print("Saliendo de la vega...")
        input("Presione cualquier tecla para continuar...")
        break