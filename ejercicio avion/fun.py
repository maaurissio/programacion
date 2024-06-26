from os import system
system("cls")

def comprar_pasajes(asientos, pasajeros):
    system("cls")
    print("Mapa de asientos:")
    print("O = Disponible\nX = Ocupado")
    for fila, asiento in asientos.items():
        print(f"Fila {fila}: {' '.join(asiento)}")
    while True:
        cantidad = input("¿Cuántos asientos desea comprar?\nCantidad: ")
        if cantidad.isnumeric():
            cantidad = int(cantidad)
            break
        else:
            print("Por favor ingrese una cantidad válida.")
    asientos_comprados = 0
    while asientos_comprados < cantidad:
        while True:
            rut = input("Ingrese el rut de la persona que ocupara el asiento: ")
            if len(rut) == 8 and rut.isnumeric():
                rut = int(rut)
                break
            else:
                print("Ingrese un rut valido")
        nombre = input("Ingrese el nombre de la persona que ocupara el asiento: ")
        apellido = input("Ingrese el apellido de la persona que ocupara el asiento: ")
        while True:
            try:
                fila = int(input("Ingrese el número de la fila (1-6): "))
                if fila >= 1 and fila <= 6:
                    break
                else:
                    print("Ingrese una fila válida.")
            except ValueError:
                print("Valor invalido")
        while True:
            try:
                asiento = int(input("Ingrese el número de asiento (1-33): "))
                if asiento >= 1 and asiento <= 33 and asientos[fila][asiento - 1] == 'O':
                    if asiento >= 1 and asiento <=5 or asiento == 18:
                        tipo_asiento = "Preferente"
                    elif (asiento >= 6 and asiento <= 9) or (asiento >= 19 and asiento <= 33):
                        tipo_asiento = "Comun"
                    else:
                        tipo_asiento = "Espacio Adicional"
                    asientos[fila][asiento - 1] = 'X'
                    asientos_comprados += 1
                    pasajero = {
                        "Rut": rut,
                        "Nombre": nombre,
                        "Apellido": apellido,
                        "Tipo asiento": tipo_asiento
                    }
                    pasajeros.append(pasajero)
                    print("El asiento fue comprado con éxito.")
                    break
                else:
                    print("Asiento no disponible, ingrese otro por favor")
            except ValueError:
                print("Valor invalido")

def mostrar_ubicaciones(asientos):
    system("cls")
    print("\nAsientos disponibles:")
    for fila, asientos_fila in asientos.items():
        asientos_libres = ""
        for i, estado in enumerate(asientos_fila):
            if estado == 'O':
                asientos_libres += str(i + 1) + ", "
        if asientos_libres:
            print(f"Fila {fila}: {asientos_libres[:-2]}")  

def ver_pasajeros(pasajeros):
    system("cls")
    for pasajero in pasajeros:
        rut = pasajero["Rut"]
        nombre = pasajero["Nombre"]
        apellido = pasajero["Apellido"]
        tipo_asiento = pasajero["Tipo asiento"]
        print(f"Rut: {rut}, Nombre: {nombre}, Apellido: {apellido}, Tipo asiento: {tipo_asiento}")

def buscar_pasajeros(pasajeros):
    system("cls")
    while True:
        rut_buscado = input("Ingrese el rut que desea buscar: ")
        if len(rut_buscado) == 8 and rut_buscado.isnumeric():
            rut_buscado = int(rut_buscado)
            break
        else:
            print("Ingrese un rut valido")
    encontrado = False 
    for pasajero in pasajeros:
        if rut_buscado == pasajero["Rut"]:
            rut = pasajero["Rut"]
            nombre = pasajero["Nombre"]
            apellido = pasajero["Apellido"]
            tipo_asiento = pasajero["Tipo asiento"]
            print(f"Rut: {rut}, Nombre: {nombre}, Apellido: {apellido}, Tipo asiento: {tipo_asiento}")
            encontrado = True
            break
    if not encontrado:
        print("Pasajero no encontrado o pasajero no existe")

def imprimir_pasajeros(pasajeros):
    t = open("archivo.txt", "w")
    for pasajero in pasajeros:
        texto = str(pasajero).replace("{", "").replace("}", "")
        t.write(texto + "\n")

