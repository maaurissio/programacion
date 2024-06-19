from os import system
system("cls")

"""
-Se requiere desarrollar una aplicacion en python para la empresa de transporte Universo. 

-Esta aplicacion debe gestionar las reservas de pasajes para buses con capacidad para 16 personas.

-El programa debe registrar por cada pasaje el rut del pasajero, y consultar si desea ventana o pasillo.

-La aplicacion debe mostrar los asientos disponibles en un menu (segun el tipo, ventana o pasillo) para hacer la reserva.

-El programa tras cada reserva, debe generar un archivo de texto con el boleto.

-El programa debe permitir la generacion de archivo CSV con todas las reservas.

-La aplicacion debe incluir una opcion para salir de ella.
"""

bus = { 1: 'Disponible', 2: 'Disponible',  
        3: 'Disponible', 4: 'Disponible',  
        5: 'Disponible', 6: 'Disponible',  
        7: 'Disponible', 8: 'Disponible',
        9: 'Disponible', 10: 'Disponible',
        11: 'Disponible', 12: 'Disponible',
        13: 'Disponible', 14: 'Disponible',
        15: 'Disponible', 16: 'Disponible' }

reservas = []

def reserva(bus, reservas):
    system("cls")
    rut = input("Ingrese su rut para la reserva: ")
    while True:
        try:
            tipo = int(input("\n1.- Ventana\n2.- Pasillo\nSeleccione opción: "))
            if tipo >= 1 and tipo <= 2:
                break
            else:
                print("Ingrese una opción válida (1 o 2).")
        except ValueError:
            print("Opción inválida. Ingrese un número.")
    system("cls")
    print("Asientos disponibles:")
    for asiento, estado in bus.items():
        if estado == "Disponible":
            print(asiento, estado)
    while True:
        try:
            op = int(input("Ingrese el número del asiento que quiere: "))
            if 1 <= op <= 16 and bus[op] == "Disponible":
                print("Asiento reservado con éxito!")
                pasajero = (rut, tipo, op)
                reservas.append(pasajero)
                bus[op] = "Reservado"
                return bus, reservas
            else:
                print("Asiento no disponible o inválido. Intente nuevamente.")
        except (ValueError, KeyError):
            print("Opción inválida. Ingrese un número de asiento válido.")

def disponibilidad(bus):
    system("cls")
    print("Asientos disponibles:")
    for asiento, estado in bus.items():
        if estado == "Disponible":
            print(asiento, estado)

while True:
    print("""Bienvenido a transporte Universo
        1.- Reservar Pasaje
        2.- Mostrar asientos disponibles
        0.- Salir
        """)
    try:
        op = input("Ingrese una opción: ")
        match op:
            case "1":
                reserva(bus, reservas)
            case "2":
                disponibilidad(bus)
            case "0":
                break
            case other:
                print("Opcion invalida, seleccione otra")
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el teclado...")
        break