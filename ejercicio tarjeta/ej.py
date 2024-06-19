from os import system
from fun import *
system("cls")

while True:
    print("""
    1. Comprar
    2. Pagar Deuda
    3. Consultar Detalles
    4. Compras Totales
    0. Salir""")
    try:
        op = input("Ingrese una opción: ")
        match op:
            case "1":
                comprar(tarjeta)
                compras += 1
            case "2":
                pago_deuda(tarjeta)
            case "3":
                consulta_detalles(tarjeta)
            case "4":
                total(compras)
            case "0":
                pass
            case other:
                print("Opcion invalida")
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el teclado")
        break