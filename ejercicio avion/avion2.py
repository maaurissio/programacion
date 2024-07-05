import os

def mostrar_menu():
    """Muestra el menú principal del sistema de reservas."""
    print("\n--- SISTEMA DE RESERVA DE PASAJES ---")
    print("1. Comprar pasajes")
    print("2. Mostrar ubicaciones disponibles")
    print("3. Ver listado de pasajeros")
    print("4. Buscar pasajero")
    print("5. Imprimir lista de pasajeros")
    print("0. Salir")

def mostrar_ubicaciones(asientos):
    """Muestra el mapa de asientos del avión."""
    print("    A B C D E F")
    for fila in range(1, 28):
        print(f"{fila:2d} ", end="")
        for col in range(6):
            asiento = asientos.get((fila, col), "O")  
            print(asiento, end=" ")
        print()

def comprar_pasajes(asientos):
    """Permite al usuario comprar pasajes."""
    while True:
        try:
            cantidad = int(input("Cantidad de pasajes a comprar: "))
            if 1 <= cantidad <= 198:
                break
            else:
                print("Cantidad inválida. Debe ser entre 1 y 198.")
        except ValueError:
            print("Ingrese un número válido.")

    mostrar_ubicaciones(asientos)
    pasajeros = []
    for _ in range(cantidad):
        while True:
            ubicacion = input("Ingrese ubicación (fila columna, ej. 1 A): ").replace(" ", "").upper()  # Eliminar espacios y convertir a mayúsculas
            try:
                fila, col = int(ubicacion[0:2]), ubicacion[2]
                if not (1 <= fila <= 27 and col in "ABCDEF"):
                    print("Ubicación inválida. Fila debe ser entre 1 y 27, columna entre A y F.")
                elif (fila, ord(col) - 65) not in asientos:  # Convertir columna a índice
                    print("Ubicación ya ocupada.")
                else:
                    break
            except (IndexError, ValueError):
                print("Formato incorrecto. Use fila (número) y columna (letra).")

        rut = input("Ingrese RUT (sin puntos ni guion): ")
        nombre = input("Ingrese nombre: ")
        apellido = input("Ingrese apellido: ")
        pasajeros.append((fila, col, rut, nombre, apellido))
        asientos[(fila, col)] = "X"  

    return pasajeros

def ver_listado_pasajeros(pasajeros):
    """Muestra el listado de pasajeros ordenados por asiento."""
    if not pasajeros:
        print("No hay pasajeros registrados.")
    else:
        for fila, col, rut, nombre, apellido in sorted(pasajeros):
            print(f"Asiento {fila:02d}{chr(col+65)}: {rut}, {nombre} {apellido}")

def buscar_pasajero(pasajeros):
    """Busca un pasajero por RUT."""
    rut = input("Ingrese RUT a buscar: ")
    for fila, col, p_rut, nombre, apellido in pasajeros:
        if p_rut == rut:
            print(f"Asiento {fila:02d}{chr(col+65)}: {rut}, {nombre} {apellido}")
            return
    print("Pasajero no encontrado.")

def imprimir_lista_pasajeros(pasajeros):
    """Imprime la lista de pasajeros en un archivo de texto."""
    with open("lista_pasajeros.txt", "w") as f:
        for fila, col, rut, nombre, apellido in sorted(pasajeros):
            f.write(f"Asiento {fila:02d}{chr(col+65)}: {rut}, {nombre} {apellido}\n")
    print("Lista de pasajeros guardada en lista_pasajeros.txt")

# Programa principal
asientos = {}  # Diccionario para almacenar el estado de los asientos
pasajeros = []  # Lista para almacenar los datos de los pasajeros

while True:
    mostrar_menu()
    opcion = input("Ingrese su opción: ")

    if opcion == "1":
        pasajeros.extend(comprar_pasajes(asientos))
    elif opcion == "2":
        mostrar_ubicaciones(asientos)
    elif opcion == "3":
        ver_listado_pasajeros(pasajeros)
    elif opcion == "4":
        buscar_pasajero(pasajeros)
    elif opcion == "5":
        imprimir_lista_pasajeros(pasajeros)
    elif opcion == "0":
        break
    else:
        print("Opción inválida.")
