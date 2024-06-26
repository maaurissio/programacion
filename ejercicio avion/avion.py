from os import system
system("cls")

asientos = {
    1: ['O'] * 33,
    2: ['O'] * 33,
    3: ['O'] * 33,
    4: ['O'] * 33,
    5: ['O'] * 33,
    6: ['O'] * 33,
}

# pasajeros = [{
#                     "Rut": 21588043,
#                     "Nombre": "Mauricio",
#                     "Apellido": "Gajardo",
#                     "Tipo asiento": "Comun"
#                 },{
#                     "Rut": 13958605,
#                     "Nombre": "Maria",
#                     "Apellido": "Vega",
#                     "Tipo asiento": "Comun"
#                 }
#                 ]

pasajeros = []

def comprar_pasajes(asientos, pasajeros):
    system("cls")
    print("Mapa de asientos:")
    print("0 = Disponible\n1 = Ocupado")
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
            fila = int(input("Ingrese el número de la fila (1-6): "))
            if fila >= 1 and fila <= 6:
                break
            else:
                print("Ingrese una fila válida.")
        while True:
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

def mostrar_ubicaciones(asientos):
    """Muestra los asientos disponibles en el mapa de asientos."""
    print("\nAsientos disponibles:")
    for fila, asientos_fila in asientos.items():
        asientos_libres = ""
        for i, estado in enumerate(asientos_fila):
            if estado == 'O':
                asientos_libres += str(i + 1) + ", "
        if asientos_libres:
            print(f"Fila {fila}: {asientos_libres[:-2]}")  

def ver_pasajeros(pasajeros):
    for pasajero in pasajeros:
        rut = pasajero["Rut"]
        nombre = pasajero["Nombre"]
        apellido = pasajero["Apellido"]
        tipo_asiento = pasajero["Tipo asiento"]
        print(f"RUT: {rut}, Nombre: {nombre}, Apellido: {apellido}, Tipo asiento: {tipo_asiento}")

def buscar_pasajeros(pasajeros):
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
            print("Rut encontrado")
            encontrado = True
            break
    if not encontrado:
        print("Rut no encontrado")

while True:
    print("""
1. Comprar pasajes
2. Mostrar ubicacion disponible
3. Ver listado de pasajeros
4. Buscar pasajero
5. Imprimir lista de pasajeros
0. Salir
""")
    try:
        op = int(input("Ingrese una opcion: "))
        match op:
            case 1:
                comprar_pasajes(asientos, pasajeros)
            case 2:
                mostrar_ubicaciones(asientos)
            case 3:
                ver_pasajeros(pasajeros)
            case 4:
                buscar_pasajeros(pasajeros)
            case 5:
                pass
            case 0:
                break
            case other:
                print("Opcion invalida")
    except ValueError:
        print("Opcion invalida")