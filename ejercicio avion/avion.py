from os import system
from fun import *
system("cls")

asientos = {
    1: ['O'] * 33,
    2: ['O'] * 33,
    3: ['O'] * 33,
    4: ['O'] * 33,
    5: ['O'] * 33,
    6: ['O'] * 33,
}

pasajeros = [{
                    "Rut": 12345678,
                    "Nombre": "Mauricio",
                    "Apellido": "Gajardo",
                    "Tipo asiento": "Comun"
                },{
                    "Rut": 98765432,
                    "Nombre": "Mario",
                    "Apellido": "Venegas",
                    "Tipo asiento": "Comun"
                }
                ]

# pasajeros = []

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
                imprimir_pasajeros(pasajeros)
            case 0:
                print("Saliendo...")
                break
            case other:
                print("Opcion invalida")
    except ValueError:
        print("Opcion invalida")