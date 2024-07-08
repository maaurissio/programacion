from os import system
from funciones import *
system("cls")

pedidos = [{
    "ID pedido": 56348,
    "Nombre": "Mauricio",
    "Apellido": "Gajardo",
    "Direccion": "Coronel 1067",
    "Sector": "Concepción",
    "Disp.6lts": 5,
    "Disp.10lts": 2,
    "Disp.20lts": 1
},{
    "ID pedido": 51595,
    "Nombre": "Vicente",
    "Apellido": "Colicheo",
    "Direccion": "Angol 69",
    "Sector": "Concepción",
    "Disp.6lts": 5,
    "Disp.10lts": 2,
    "Disp.20lts": 1
}]

sectores = ("Concepción", "Chiguayante", "Talcahuano", "Hualpén", "San Pedro")

while True:
    print("""
    1. Registrar pedido
    2. Listar los todos los pedidos
    3. Imprimir hoja de ruta
    4. Buscar un pedido por ID
    5. Salir del programa
        """)
    op = input("Ingrese una opcion: ")
    match op:
        case"1":
            registro_pedido(pedidos)
        case"2":
            listar(pedidos)
        case"3":
            imprimir_ruta(pedidos)
        case"4":
            buscar_pedido(pedidos)
        case"0":
            break
        case other:
            print("Opcion invalida, por favor ingrese una opcion valida")
